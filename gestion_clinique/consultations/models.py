from django.db import models
from patients.models import Patient
from users.models import Utilisateur
from medecins.models import Medecin
from parametrage.models import Acte, Medicament

# Create your models here.

class Consultation(models.Model):
    code_consultation = models.CharField(max_length=20, unique=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Qui a enregistré
    date_consultation = models.DateTimeField()
    date_fin_validite_consultation = models.DateTimeField()

    actes = models.ManyToManyField(Acte, blank=True)  # les actes effectués
    

    def save(self, *args, **kwargs):
        if not self.code_consultation:
            last_id = Consultation.objects.all().count() + 1
            self.code_consultation = f"CONS{last_id:04d}"
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Consultation {self.code_consultation} - {self.patient}"

class Ordonnance(models.Model):
    code_ordonnance = models.CharField(max_length=20, unique=True, blank=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    date_ordonnance = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.code_ordonnance:
            last_id = Ordonnance.objects.all().count() + 1
            self.code_ordonnance = f"ORD{last_id:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code_ordonnance

class OrdonnanceDetail(models.Model):
    ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    posologie_medicament = models.TextField()

    def __str__(self):
        return f"{self.ordonnance} - {self.medicament}"
