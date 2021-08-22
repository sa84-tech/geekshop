from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    activation_key = models.CharField(
        max_length=128,
        blank=True
    )

    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=24))
    )

    @property
    def is_activation_key_expired(self):
        return now() > self.activation_key_expires
