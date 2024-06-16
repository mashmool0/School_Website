from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class Storage(models.Model):
    my_file = models.FileField()


path = default_storage.save('/example.txt', ContentFile(b'Storage'))
