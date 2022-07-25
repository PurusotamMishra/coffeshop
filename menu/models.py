from django.db import models

# Create your models here.

class CoffeeMenu(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')

class TeaMenu(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')

class CakeMenu(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')