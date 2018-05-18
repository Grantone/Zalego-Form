from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Signer(models.Model):
    user = models.ForeignerKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    languages = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
