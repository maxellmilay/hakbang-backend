from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.utils.neural_network.train import train

class Command(BaseCommand):
    help = 'Calculate All Accessibility Scores'

    def handle(self, *args, **options):
        try:
            train()
            self.stdout.write(self.style.SUCCESS(f'Successfully trained neural network model'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
