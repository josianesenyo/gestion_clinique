from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Personne(models.Model):
    CIVILITE_CHOICES = (
        ('M', 'Monsieur'),
        ('Mme', 'Madame'),
    )


    code = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    civilite = models.CharField(max_length=10, choices=CIVILITE_CHOICES)

    class Meta:
        abstract = True


class Secretaire(Personne):
    utilisateur = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    titre_secretaire = models.CharField(max_length=100, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.code:
            last_id = Secretaire.objects.all().count() + 1
            self.code = f"SEC{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Secrétaire {self.nom} {self.prenom}"
