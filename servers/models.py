from django.db import models


class Server(models.Model):
    server_name = models.CharField(max_length=200)
    server_owner = models.CharField(max_length=200)
    server_address = models.URLField(max_length=200)
    server_description = models.TextField()
    server_votes = models.IntegerField(default = 0)
    server_mt_version = models.CharField(max_length=10)
