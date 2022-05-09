from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='активна',
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        verbose_name='категория',
    )
    name = models.CharField(
        verbose_name='имя',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )
    short_desc = models.CharField(
        max_length=256,
        blank=True,
        verbose_name='краткое описание',
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание',
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    qtty = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name='активен',
        default=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print(f'Product Save: ID: {self.pk} QTTY: {self.qtty}')
        super(self.__class__, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def split_description(self):
        descriptions = self.description.split(';')
        return list(map(lambda s: s.strip(), descriptions))

    @staticmethod
    def get_items():
        return Product.objects.all()

    @staticmethod
    def get_popular_products():
        _items = Product.get_items()
        return list(_items.order_by('price').values())[:3]

    @staticmethod
    def get_new_products():
        _items = Product.get_items()
        return list(_items.order_by('-id').values())[:3]


class Contact(models.Model):
    location = models.CharField(
        verbose_name='населенный пункт',
        max_length=64,
    )
    phone = models.CharField(
        verbose_name='телефон',
        max_length=16,
        blank=True,
    )
    email = models.CharField(
        verbose_name='электронная почта',
        max_length=64,
        blank=True,
    )
    address = models.CharField(
        verbose_name='адрес',
        max_length=256,
        blank=True,
    )

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
