from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    email = models.EmailField(blank=False, unique=True)
    mailings = models.BooleanField(default=False, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=123, blank=True, null=True)

    def __str__(self):
        return f'{self.username}'
