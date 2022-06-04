from distutils.command.upload import upload
from django.db import models

# Create your models here.
class PhotoImageModel(models.Model):
    user_image = models.ImageField(
        verbose_name='img',
        blank = True,
        null = True
        )
        