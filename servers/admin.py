from django.contrib import admin

from .models import Server
from.models import Tag


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


admin.site.register(Server, ServerAdmin)
admin.site.register(Tag)