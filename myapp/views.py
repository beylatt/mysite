from django.shortcuts import render, get_object_or_404
from .models import Product, NewsArticle

# Главная страница
def home(request):
    articles = NewsArticle.objects.all()  # Получаем все статьи
    return render(request, 'myapp/home.html', {'articles': articles})

#Список продуктов
def product_list(request):
    products = Product.objects.all()  # Получаем все продукты
    return render(request, 'myapp/product_list.html', {'products': products})


# Детальная информация о продукте
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})

from django.utils import timezone
from django.shortcuts import render

def home(request):
    timestamp = int(timezone.now().timestamp())
    return render(request, 'myapp/home.html', {'timestamp': timestamp})