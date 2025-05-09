from django.db import models

# Create your models here.

class TypeActe(models.Model):
    code = models.IntegerField(unique=True)
    libelle = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.code:
            last_id = TypeActe.objects.all().count() + 1
            self.code = f"TYP{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.libelle

class Acte(models.Model):
    code_acte = models.CharField(max_length=20, unique=True, blank=True)
    libelle_acte = models.CharField(max_length=100)
    montant_acte = models.DecimalField(max_digits=10, decimal_places=2)
    type_acte = models.ForeignKey(TypeActe, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.code_acte:
            last_id = Acte.objects.all().count() + 1
            self.code_acte = f"ACT{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.libelle_acte

class Medicament(models.Model):
    code_medicament = models.CharField(max_length=20, unique=True, blank=True)
    libelle_medicament = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.code_medicament:
            last_id = Medicament.objects.all().count() + 1
            self.code_medicament = f"MEDIC{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.libelle_medicament
