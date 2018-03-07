from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from servers.models import Server
from mods.models import Mod


class Notification(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    stared_mods = models.ManyToManyField(Mod, verbose_name='Mods',  blank=True)
    stared_servers = models.ManyToManyField(Server, verbose_name='Servers',  blank=True)
    notifications = models.ManyToManyField(Notification, verbose_name='Notification', blank=True)
    # ----- Communication -----
    github = models.TextField(max_length=50, blank=True)
    irc = models.TextField(max_length=50, blank=True)
    discord = models.TextField(max_length=50, blank=True)
    skype = models.TextField(max_length=50, blank=True)
    ingame = models.TextField(max_length=50, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
