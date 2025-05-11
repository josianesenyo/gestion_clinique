from patients.models import Personne
from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
# Create your models here.

class Medecin(Personne):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    titre_medecin = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.code:
            last_id = Medecin.objects.all().count() + 1
            self.code = f"MED{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Dr. {self.nom} {self.prenom}"

class Specialite(models.Model):
    code = models.CharField(max_length=20, unique=True , blank=True)
    libelle = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.code:
            last_id = Specialite.objects.all().count() + 1
            self.code = f"SPE{last_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.libelle

class AffecterSpecialite(models.Model):
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    date_affectation = models.DateField()
    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.medecin} - {self.specialite}"
