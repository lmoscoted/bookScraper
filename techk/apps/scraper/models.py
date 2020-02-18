# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
            return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    product_description = models.CharField(max_length=2000)
    price = models.CharField(max_length=50) 
    category = models.ForeignKey(Category, related_name='books',on_delete=models.CASCADE) # Foreign Key 
    upc = models.CharField(max_length=50)
    stock = models.PositiveIntegerField() # Positive Integer
    thumbnail = models.URLField(max_length=200)

    def __str__(self):
        return self.name            