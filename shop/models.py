from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to = "shop/", blank=True, null=True)