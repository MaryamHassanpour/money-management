from django.db import models
from django.contrib.auth.models import User
from base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30, null=True, blank=True)
    symbol = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
