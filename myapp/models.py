from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Название продукта
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    description = models.TextField()  # Описание продукта
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.name
from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
