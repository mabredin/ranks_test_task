from django.urls import path

from item import views


app_name = 'main'
urlpatterns = [
    path('', views.ItemListView.as_view()),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item'),
    path('success/', views.page_success),
    path('cancel/', views.page_cancel),
]
