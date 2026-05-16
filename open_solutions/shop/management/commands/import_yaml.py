import yaml

from django.core.management.base import BaseCommand
from django.db import transaction

from shop.models import (
    Shop,
    Category,
    Product,
    ShopProduct,
    Parameter,
    ProductParameter,
)


class Command(BaseCommand):
    help = "Импорт товаров из YAML-файла"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        file_path = options["file_path"]

        with open(file_path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        shop, _ = Shop.objects.get_or_create(
            name=data["shop"],
            defaults={
                "url": "",
                "phone": "",
            },
        )

        categories = {}

        for category_data in data.get("categories", []):
            category, _ = Category.objects.get_or_create(
                id=category_data["id"],
                defaults={
                    "name": category_data["name"],
                },
            )
            categories[category_data["id"]] = category

        for item in data.get("goods", []):
            category = categories.get(item["category"])

            product, _ = Product.objects.update_or_create(
                id=item["id"],
                defaults={
                    "category": category,
                    "name": item["name"],
                    "description": item.get("model", ""),
                },
            )

            shop_product, _ = ShopProduct.objects.update_or_create(
                product=product,
                shop=shop,
                defaults={
                    "quantity": item.get("quantity", 0),
                    "price": item.get("price", 0),
                    "price_rrc": item.get("price_rrc", 0),
                    "description": item.get("model", ""),
                },
            )

            ProductParameter.objects.filter(shop_product=shop_product).delete()

            for param_name, param_value in item.get("parameters", {}).items():
                parameter, _ = Parameter.objects.get_or_create(
                    name=param_name,
                    defaults={
                        "unit": "",
                    },
                )

                ProductParameter.objects.create(
                    shop_product=shop_product,
                    parameter=parameter,
                    value=str(param_value),
                )

        self.stdout.write(self.style.SUCCESS(f"Импорт завершён: {file_path}"))
