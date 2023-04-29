from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

from mainapp.models import Product


class Order(models.Model):

    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    PROCEEDED = 'PRD'
    PAID = 'ID'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (PROCEEDED, 'оплачен'),
        (PAID, 'обрабатывается'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    created = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name='обновлен',
        auto_now=True,
        choices=ORDER_STATUS_CHOICES,
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS_CHOICES,
        default=FORMING,
    )

    is_active = models.BooleanField(
        verbose_name='активен',
        default=True,
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Текущий заказ: {self.id}'

    @cached_property
    def get_related_cached(self):
        return self.orderitems.select_related()

    def get_total_qtty(self):
        _items = self.get_related_cached
        return sum(list(map(lambda x: x.qtty, _items)))

    def get_total_cost(self):
        _items = self.get_related_cached
        return sum(list(map(lambda x: x.qtty * x.product.price, _items)))

    def get_summary(self):
        _items = self.get_related_cached
        return {
            'total_cost': sum(list(map(lambda x: x.qtty * x.product.price, _items))),
            'total_qtty': sum(list(map(lambda x: x.qtty, _items))),
            'updated': self.updated,
            'created': self.created,
            'items': _items,
        }

    def get_product_type_qtty(self):
        _items = self.get_related_cached
        return len(_items)

    def delete(self):
        _items = self.get_related_cached
        for item in _items:
            item.product.qtty += item.qtty
            item.product.save()

        self.is_active = False
        self.save()


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        related_name='orderitems',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        verbose_name='продукт',
        on_delete=models.CASCADE,
    )

    qtty = models.PositiveIntegerField(
        verbose_name='количество',
        default=1,
    )

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.filter(pk=pk).first()

    def get_product_cost(self):
        return self.product.price * self.qtty
