from django.db import models

# Create your models here.

class Personne(models.Model):
    CIVILITE_CHOICES = (
        ('M', 'Monsieur'),
        ('Mme', 'Madame'),
    )

    code = models.CharField(max_length=20, unique=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    civilite = models.CharField(max_length=10, choices=CIVILITE_CHOICES)

    class Meta:
        abstract = True

class Patient(Personne):
    date_enreg = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            last_id = Patient.objects.all().count() + 1
            self.code = f"PAT{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.nom} {self.prenom}"
