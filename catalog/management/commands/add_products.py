from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to the database'

    def handle(self, *args, **options):
        category, created = Category.objects.get_or_create(
            name="Телевизоры",
            defaults={"description": "Современные телевизоры"},
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Категория '{category.name}' создана"))
        else:
            self.stdout.write(self.style.WARNING(f"Категория '{category.name}' уже существует"))

        products = [
            {"name": "Samsung QLED 55", "price": 70000, "description": "55 дюймов, 4K QLED"},
            {"name": "LG OLED 65", "price": 120000, "description": "65 дюймов, OLED, 4K HDR"},
            {"name": "Sony Bravia 50", "price": 85000, "description": "50 дюймов, 4K HDR"},
        ]

        for prod in products:
            product, created = Product.objects.get_or_create(
                name=prod["name"],
                category=category,
                defaults={
                    "price": prod["price"],
                    "description": prod["description"],
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Продукт '{product.name}' добавлен"))
            else:
                self.stdout.write(self.style.WARNING(f"Продукт '{product.name}' уже существует"))

