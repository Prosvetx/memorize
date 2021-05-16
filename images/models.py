from django.db import models

from utils.models.upload_path_generator import image_name_path_generator


class Image(models.Model):
    title = models.CharField(max_length=120)
    file = models.ImageField(upload_to=image_name_path_generator)

    def __str__(self):
        return self.title

