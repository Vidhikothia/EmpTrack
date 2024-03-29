from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Employee(AbstractUser):
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    objects = UserManager()

    def __str__(self):
        return (str(self.username))
