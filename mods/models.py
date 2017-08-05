from django.db import models
from django.contrib.auth.models import User
from minetestdb import *


class Mod(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User)
    git = models.URLField(max_length=200)
    mt_version = models.CharField(max_length=10)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, verbose_name='Tags')