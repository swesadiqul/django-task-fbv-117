from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name


class Service(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='services')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    



