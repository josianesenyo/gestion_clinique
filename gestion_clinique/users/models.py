from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Utilisateur(AbstractUser):
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.username
