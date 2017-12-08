from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Mod(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, None)
    git = models.URLField(max_length=200, null=True)
    download = models.URLField(max_length=200, null=True)
    mt_version = models.CharField(max_length=10)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, verbose_name='Tags',  blank=True)
