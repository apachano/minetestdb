from django.contrib import admin

from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


admin.site.register(Server, ServerAdmin)