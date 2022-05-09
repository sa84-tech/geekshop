from django.core.management import BaseCommand
from django.db import connection
from django.db.models import Q

from adminapp.views_api import db_profile_by_type
from mainapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_products = Product.objects.filter(
            Q(category__name='офис') |
            Q(category__name='классика')
        )

        print(test_products)

        db_profile_by_type('learn db', '', connection.queries)
