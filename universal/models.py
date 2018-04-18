from django.db import models


class Version(models.Model):
    objattr = models.CharField(max_length=11, default="mt_version") #NOTE DO NOT EDIT
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value
