from django.db import models
from consultations.models import Consultation
from parametrage.models import Acte
from users.models import Utilisateur

# Create your models here.

class Facture(models.Model):
    code_facture = models.CharField(max_length=20, unique=True, blank=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, null=True, blank=True)
    type_facture = models.CharField(max_length=100, blank=True)
    date_enreg_facture = models.DateTimeField()
    date_paiement_facture = models.DateTimeField(null=True, blank=True)
    montant_facture = models.DecimalField(max_digits=10, decimal_places=2)
    montant_paye_facture = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    valide_par = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True, related_name='factures_validées')

    def save(self, *args, **kwargs):
        if not self.code_facture:
            last_id = Facture.objects.all().count() + 1
            self.code_facture = f"FACT{last_id:04d}"
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.code_facture

class FactureDetail(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    acte = models.ForeignKey(Acte, on_delete=models.CASCADE)
    montant_facture_detail = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.facture} - {self.acte}"

class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentDate = models.DateTimeField()

    def __str__(self):
        return f"{self.facture} - {self.amount}"
