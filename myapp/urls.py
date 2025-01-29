from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('products/', views.product_list, name='product_list'),  # Список продуктов
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  # Детальная страница
]