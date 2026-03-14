from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    # Исправлено max_lenght на max_length
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории" # Поправил склонение (множественное число)
    
# Исправлено models.model на models.Model
class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория")
    
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    city = models.CharField(max_length=100, verbose_name="Город")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    
    image = models.ImageField(upload_to='ads_photos/', blank=True, null=True, verbose_name="Фото")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"