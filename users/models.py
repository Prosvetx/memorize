from django.core.validators import RegexValidator
from django.db import models

from django.contrib.auth.models import AbstractUser

from intrests.models import Intrest


class User(AbstractUser):
    intrests = models.ManyToManyField(Intrest, related_name='intrests', blank=True)
    phone_number = models.CharField(max_length=12, validators=[RegexValidator('[+]7\d{10}$')], blank=True)

