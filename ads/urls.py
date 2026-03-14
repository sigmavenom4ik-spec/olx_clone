from django.urls import path
from . import views

urlpatterns =[
    # Пустая строка '' означает главную страницу
    path('', views.ad_list, name='ad_list'),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
]