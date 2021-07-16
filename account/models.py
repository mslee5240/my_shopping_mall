from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    university = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to = "account/", blank=True, null=True)
