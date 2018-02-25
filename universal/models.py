from django.db import models


class Version(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value
