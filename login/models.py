from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Phone(models.Model):
    phone_no = models.IntegerField()
