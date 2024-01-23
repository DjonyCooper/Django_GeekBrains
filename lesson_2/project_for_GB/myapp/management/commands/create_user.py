from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = 'Create user.'

    def handle(self, *args, **kwargs):
        user = User(name='Семен', email='Semen@gmail.com', phone='+78005553535', address='Московская обл., г.Раменское, ул.Театральная, д.85', date_registry='1990-01-01')
        user.save()
        self.stdout.write(f'{user}')