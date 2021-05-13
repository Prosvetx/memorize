from django.db import models


class Intrest(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title
