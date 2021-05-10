from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.db import models, transaction

from django.contrib.auth.models import AbstractUser


class Intrest(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('Адрес электронной почты должен быть установлен.')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

class User(AbstractUser):
    intrests = models.ManyToManyField('Intrest', related_name='intrests', blank=True)
    phone_number = models.CharField(max_length=12, validators=[RegexValidator('[+]7\d{10}$')], blank=True)

    objects = UserManager()
