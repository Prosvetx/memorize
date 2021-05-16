from django.db import models

from images.models import Image
from materials.models.subdivision import Subdivision
from tags.models import Tag


class Theme(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000, null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image, related_name='themes', blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.title
