from django.contrib import admin

from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'server_owner')


admin.site.register(Server, ServerAdmin)