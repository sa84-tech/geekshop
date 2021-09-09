from functools import reduce

from django.db import models
from django.conf import settings

from mainapp.models import Product
from ordersapp.models import OrderItem


# class CartQuerySet(models.QuerySet):
#     def delete(self, *args, **kwargs):
#         for object in self:
#             object.product.qtty += object.qtty
#             object.product.save()
#         super(CartQuerySet, self).delete(*args, **kwargs)


class Cart(models.Model):
    # objects = CartQuerySet.as_manager()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    qtty = models.PositiveIntegerField(
        verbose_name='количество',
        default=1,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    @staticmethod
    def get_item(pk):
        return Cart.objects.filter(pk=pk).first()

    @property
    def product_cost(self):
        print(self.product.price * self.qtty)
        return self.product.price * self.qtty

    @staticmethod
    def count(user):
        items = list(user.cart.values('qtty'))
        return reduce(lambda summ, item: summ + item['qtty'], items, 0)

    @staticmethod
    def total(user):
        items = list(user.cart.values('qtty', 'product__price'))
        return reduce(lambda summ, item: summ + item['qtty'] * item['product__price'], items, 0)

    @staticmethod
    def get_cart(user):
        cart = user.cart.values('pk', 'product', 'product__name', 'product__image', 'product__price', 'qtty')
        cart_items = map(lambda item: {**item, 'cost': item['product__price'] * item['qtty']}, cart)
        return list(cart_items)

    @staticmethod
    def delete_items(user):
        Cart.objects.filter(user=user).delete()

