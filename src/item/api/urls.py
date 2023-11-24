from django.urls import path

from . import views


urlpatterns = [
    path('buy/<int:pk>/', views.CreateCheckoutSessionView.as_view()),
]
