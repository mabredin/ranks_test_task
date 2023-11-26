from django.urls import path

from . import views

urlpatterns = [
    path("buy/<int:pk>/", views.CreateCheckoutSessionForItemView.as_view()),
    path("buy/order/<int:pk>/", views.CreateCheckoutSessionForOrderView.as_view()),
]
