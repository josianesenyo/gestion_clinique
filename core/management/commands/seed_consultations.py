from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from datetime import timedelta
from django.utils import timezone

from consultations.models import Consultation
from medecins.models import Medecin
from parametrage.models import Acte
from patients.models import Patient

class Command(BaseCommand):
    help = 'Génère des consultations fictives'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        patients = Patient.objects.all()
        medecins = Medecin.objects.all()
        actes = list(Acte.objects.all())

        if not patients or not medecins or not actes:
            self.stdout.write(self.style.ERROR('Veuillez d’abord créer quelques patients, médecins et actes.'))
            return

        for _ in range(20):  # Crée 20 consultations
            patient = random.choice(patients)
            medecin = random.choice(medecins)
            code = f'CST-{random.randint(1000, 9999)}'

            consultation = Consultation.objects.create(
                code_consultation=code,
                patient=patient,
                medecin=medecin,
                date_consultation=timezone.now() - timedelta(days=random.randint(0, 30)),
                date_fin_validite_consultation=timezone.now() + timedelta(days=random.randint(5, 20))
            )

            random_actes = random.sample(actes, k=random.randint(1, min(3, len(actes))))
            consultation.actes.set(random_actes)

        self.stdout.write(self.style.SUCCESS('20 consultations créées avec succès !'))
