from django.db import models

from django.conf import settings
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

    @property
    def get_total_quantity(self):
        items = self.orderitems.select_related()

    @property
    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    @property
    def get_total_cost(self):
        items = self.oredereditems.select_relatied()

        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    @property
    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
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

    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=1,
    )

    @property
    def get_product_cost(self):
        return self.product.price * self.quantity
