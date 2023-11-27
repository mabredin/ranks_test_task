from django.db import models
from django.db.models.aggregates import Count
from django.urls import reverse
from stripe.api_resources.checkout import Session


class Item(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Введите название товара",
        null=False,
        verbose_name="Название",
    )
    description = models.TextField(
        help_text="Введите описание товара",
        verbose_name="Описание",
        blank=True
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Введите стоимость товара в рублях",
        verbose_name="Стоимость",
        null=False,
    )

    def __str__(self):
        return self.get_full_name()

    def to_stripe_line_item(self) -> Session.CreateParamsLineItem:
        return {
            "price_data": {
                "currency": "rub",
                "product_data": {
                    "name": self.name,
                    "description": self.description if self.description else None,
                },
                "unit_amount_decimal": self.price * 100,
            },
            "quantity": 1,
        }

    def to_stripe_line_items(self) -> list[Session.CreateParamsLineItem]:
        return [self.to_stripe_line_item()]

    def get_full_name(self):
        return f"ID: {self.id} - {self.name} {self.price}"

    def get_absolute_url(self):
        return reverse("main:item", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "item"


class Order(models.Model):
    items = models.ManyToManyField(
        Item, through="OrderItemRelation", related_name="order"
    )

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse("main:order", kwargs={"pk": self.pk})

    def to_stripe_line_items(self) -> list[Session.CreateParamsLineItem]:
        items = self.items.annotate(count=Count("item_order")).values(
            "name", "description", "price", "count"
        )
        return [
            {
                "price_data": {
                    "currency": "rub",
                    "product_data": {
                        "name": item["name"],
                        "description": item["description"] if item["description"] else None,
                    },
                    "unit_amount_decimal": item["price"] * 100,
                },
                "quantity": item["count"],
            }
            for item in items
        ]

    def display_items(self):
        return ", ".join([str(item.name) for item in self.items.all()])

    display_items.short_description = "Items"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        db_table = "order"


class OrderItemRelation(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.PROTECT, related_name="item_order", null=False
    )
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="order_item", null=False
    )

    def __str__(self):
        return f"{self.order.id} - {self.item.name}"

    class Meta:
        db_table = "orderitemrelation"
        verbose_name = "Товар-Заказ"
        verbose_name_plural = "Товары-Заказы"
