from django.contrib import admin

from item.models import Item, Order, OrderItemRelation


class OrderItemRelationInline(admin.TabularInline):
    model = OrderItemRelation
    extra = 1


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    inlines = [OrderItemRelationInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "display_items")
    list_display_links = ("id",)
    search_fields = ("items",)
    inlines = [OrderItemRelationInline]


@admin.register(OrderItemRelation)
class OrderItemRelationAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "item")
    list_display_links = ("id",)
    search_fields = ("order__id", "item__name")
    list_filter = ("item__name",)
