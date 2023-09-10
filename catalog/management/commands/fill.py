import json

from django.core.management import BaseCommand

from catalog.models import Category, Product
from config.settings import BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open(BASE_DIR / 'catalog/fixtures/category.json', 'r', encoding='cp1251') as file:
            category_data = json.load(file)
            for item in category_data:
                Category.objects.create(
                    pk=item['pk'],
                    title=item['fields']['title'],
                    description=item['fields']['description']
                )
