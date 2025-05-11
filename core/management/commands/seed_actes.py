from django.core.management.base import BaseCommand
import random

from parametrage.models import Acte

class Command(BaseCommand):
    help = "Génère des actes médicaux fictifs"

    def handle(self, *args, **kwargs):
        actes = [
            ("ACT-100", "Consultation générale"),
            ("ACT-101", "Radiographie"),
            ("ACT-102", "Analyse sanguine"),
            ("ACT-103", "Vaccination"),
            ("ACT-104", "Pansement"),
            ("ACT-105", "Échographie"),
            ("ACT-106", "Consultation gynécologique"),
            ("ACT-107", "Électrocardiogramme")
        ]

        for code, nom in actes:
            Acte.objects.get_or_create(code=code, nom=nom)

        self.stdout.write(self.style.SUCCESS(f"{len(actes)} actes créés avec succès."))
