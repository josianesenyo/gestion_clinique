from django.core.management.base import BaseCommand
from django_seed import Seed
import random

from patients.models import Patient

class Command(BaseCommand):
    help = 'Génère des patients fictifs'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        sexes = ['M', 'F']

        for _ in range(20):
            Patient.objects.create(
                nom=seeder.faker.last_name(),
                prenom=seeder.faker.first_name(),
                sexe=random.choice(sexes),
                date_naissance=seeder.faker.date_of_birth(minimum_age=0, maximum_age=90),
                adresse=seeder.faker.address(),
                telephone=seeder.faker.phone_number()
            )

        self.stdout.write(self.style.SUCCESS("20 patients créés avec succès."))
