# Generated by Django 4.1 on 2023-11-26 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0002_order_orderitemrelation_order_items"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="orderitemrelation",
            options={
                "verbose_name": "Товар-Заказ",
                "verbose_name_plural": "Товары-Заказы",
            },
        ),
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(
                blank=True, help_text="Введите описание товара", verbose_name="Описание"
            ),
        ),
    ]