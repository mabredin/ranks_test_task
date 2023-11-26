from django.urls import path

from item import views

app_name = "main"
urlpatterns = [
    path("", views.main_page, name="main"),
    path("item/", views.ItemListView.as_view(), name="item_list"),
    path("item/<int:pk>/", views.ItemDetailView.as_view(), name="item"),
    path("order/", views.OrderListView.as_view(), name="order_list"),
    path("order/<int:pk>/", views.OrderDetailView.as_view(), name="order"),
    path("success/", views.page_success),
    path("cancel/", views.page_cancel),
]
