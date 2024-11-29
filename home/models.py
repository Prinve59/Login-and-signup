from django.db import models
from django.contrib.auth.models import AbstractUser
from home.manager import(CustomManager)

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=15, default='SuperUser', unique=True)
    email = models.EmailField("email_address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomManager()

    def __str__(self):
        return self.username
