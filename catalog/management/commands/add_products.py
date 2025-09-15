from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Delete and Add products to the database"

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем данные из фикстуры
        self.stdout.write("Очищаем таблицы")
        call_command("loaddata", "catalog_fixture.json")

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены!"))
