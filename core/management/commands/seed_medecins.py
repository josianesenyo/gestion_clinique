from django.core.management.base import BaseCommand
from django_seed import Seed

from medecins.models import Medecin

class Command(BaseCommand):
    help = 'Génère des médecins fictifs'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        for _ in range(10):
            Medecin.objects.create(
                nom=seeder.faker.last_name(),
                prenom=seeder.faker.first_name(),
                specialite=seeder.faker.job()
            )

        self.stdout.write(self.style.SUCCESS("10 médecins créés avec succès."))
