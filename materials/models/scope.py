from django.db import models


class Scope(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
