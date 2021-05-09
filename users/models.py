from django.db import models
from django.contrib.auth.models import User, UserManager


class AbstractUser(User):
    intrests = models.ManyToManyField('Intrest', related_name='intrests')

    pass


class Intrest(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title
