from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def handle(self, *args, **kwargs):
        product = Product(name='Лосьон после бритья', price=265.8778, description='Лосьон после бритья Nivea for Men', how_many=200, date_create='2018-02-28')
        product.save()
        self.stdout.write(f'{product}')