from django.db import models

class Product(models.Model):
    cost = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    count = models.PositiveIntegerField()
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    company_name = models.CharField(max_length=30)
    discount = models.IntegerField()
    rating = models.PositiveIntegerField()
