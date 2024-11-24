from django.urls import path
from .views import register, login_view, logout_view

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

#Добавить  также ссылки в главный файл URL проекта shop/urls.py:

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # добавляем пути для users
    path('', include('news.urls')),  # Здесь будет основное приложение для новостей
]

Ш
