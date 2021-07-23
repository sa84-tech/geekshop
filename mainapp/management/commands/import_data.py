import json
import os

from django.core.management import BaseCommand

from authapp.models import ShopUser
from geekshop.settings import BASE_DIR
from mainapp.models import Product, ProductCategory, Contact


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            file_path = os.path.join(BASE_DIR, 'mainapp', 'data/init.json')

            with open(file_path, 'r', encoding='utf-8') as read_file:
                data = json.load(read_file)

            if data['categories']:
                for category in data['categories']:

                    new_category, create = ProductCategory.objects.get_or_create(**category)
                    if create:
                        new_category.save()
                        print(f'** Category created ** {new_category}')
                    else:
                        print(f'** Category already exists ** {new_category}')

            if data['products']:
                for product in data['products']:
                    category, create = ProductCategory.objects.get_or_create(name=product['category'])
                    if create:
                        category.save()
                    product['category'] = category
                    new_product, create = Product.objects.get_or_create(**product)

                    if create:
                        new_product.save()
                        print(f'** Product created ** {new_product}')
                    else:
                        print(f'** Product already exists ** {new_product}')

            if data['contacts']:
                for contact in data['contacts']:

                    new_contact, create = Contact.objects.get_or_create(**contact)
                    if create:
                        new_contact.save()
                        print(f'** Contact created ** {new_contact}')
                    else:
                        print(f'** Contact already exists ** {new_contact}')

            super_user = ShopUser.objects.create_superuser('admin', 'admin@example.com', 'admin', age=36)
            print(f'** user created ** {super_user}')

        except IOError:
            print(str(IOError))
            return
