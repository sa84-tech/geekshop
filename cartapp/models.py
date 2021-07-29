from functools import reduce

from django.db import models
from django.conf import settings

from mainapp.models import Product


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
        items = list(user.cart.values('qty'))
        return reduce(lambda summ, item: summ + item['qty'], items, 0)

    @staticmethod
    def total(user):
        items = list(user.cart.values('qty', 'product__price'))
        return reduce(lambda summ, item: summ + item['qty'] * item['product__price'], items, 0)
