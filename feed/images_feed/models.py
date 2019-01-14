from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


class Feed(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(storage=fs, upload_to='photos', blank=True, null=True)
    description = models.TextField(blank=True, null=True, default=None)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
