from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import AbstractUser


class Intrest(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title


class User(AbstractUser):
    intrests = models.ManyToManyField('Intrest', related_name='intrests')
    phone_number = models.CharField(max_length=12, validators=[RegexValidator('[+]7\d{10}$')], blank=True)

