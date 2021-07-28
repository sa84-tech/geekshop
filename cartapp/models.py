from functools import reduce

from django.db import models
from django.conf import settings

from mainapp.models import Product
from authapp.models import ShopUser


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    qty = models.PositiveIntegerField(
        verbose_name='количество',
        default=1,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    @staticmethod
    def count(user):
        count = 0
        for e in list(user.cart.all().values()):
            count += e['qty']
        return count
