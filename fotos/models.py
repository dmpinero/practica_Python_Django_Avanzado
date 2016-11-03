from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from practica_Python_Django_Avanzado.settings import DEFAULT_IMAGE_OPTIONS


class Foto(models.Model):

    owner = models.ForeignKey(User)
    description = models.TextField()
    image = models.ImageField()
    image = ThumbnailerImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image_resized = models.BooleanField(default=False)
