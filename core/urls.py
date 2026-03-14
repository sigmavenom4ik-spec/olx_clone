from django.contrib import admin
from django.urls import path, include  # ВАЖНО: добавь слово include сюда!

urlpatterns =[
    path('admin/', admin.site.urls),
    # Добавляем вот эту строчку. Она говорит: "Все запросы отправляй в приложение ads"
    path('', include('ads.urls')), 
]