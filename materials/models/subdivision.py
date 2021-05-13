from django.db import models

from materials.models import Scope


class Subdivision(models.Model):
    title = models.CharField(max_length=150)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
