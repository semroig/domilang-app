from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    native_lan = models.CharField(max_length=24, default='none')
    foto = models.CharField(max_length=24, default='none')
    pais = models.CharField(max_length=24, default='none')
    franja = models.CharField(max_length=24, default='none')
    nivel = models.CharField(max_length=24, default='none')
    study_lan = models.CharField(max_length=24, default='none')
    phone = models.CharField(max_length=24, default='none')