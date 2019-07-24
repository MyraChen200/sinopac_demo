from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    gender_type = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    phone = models.CharField(max_length=256, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_type, blank=True, null=True)
    age = models.PositiveIntegerField(null=False, blank=False)
