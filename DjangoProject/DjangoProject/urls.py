from django.contrib import admin
from django.urls import path, include  # Додаємо include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Підключаємо маршрути з main/urls.py
]


