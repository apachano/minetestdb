from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Server(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=True)
    address = models.URLField(max_length=200, null=True)
    website = models.URLField(max_length=200, null=True)
    description = models.TextField(null=True)
    votes = models.IntegerField(default=0, null=True)
    mt_version = models.CharField(max_length=10, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags',  blank=True)

