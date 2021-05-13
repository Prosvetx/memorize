from django.db import models

from users.models import User


class Scope(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
