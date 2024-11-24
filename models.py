#В файле users/models.py:

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Если нужны дополнительные поля
    pass

#После этого нужно зарегистрировать модель в settings.py:

# Используем свою модель пользователя
AUTH_USER_MODEL = 'users.CustomUser'
