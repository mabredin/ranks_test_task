from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from config import settings

from .models import Item, Order


class ItemListView(ListView):
    model = Item
    template_name = "item/list_items.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "item/item.html"

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
        return context


class OrderListView(ListView):
    model = Order
    template_name = "item/list_orders.html"


class OrderDetailView(DetailView):
    model = Order
    template_name = "item/order.html"

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["stripe_public_key"] = settings.STRIPE_PUBLIC_KEY
        return context


def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, "item/main.html")


def page_success(request: HttpRequest) -> HttpResponse:
    return render(request, "item/success.html")


def page_cancel(request: HttpRequest) -> HttpResponse:
    return render(request, "item/cancel.html")
