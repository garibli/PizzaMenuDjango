from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=250)
    price=models.IntegerField()