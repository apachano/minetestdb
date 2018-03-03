from django.contrib import admin

from .models import Version


class UniversalAdmin(admin.ModelAdmin):
    field = 'Version'


admin.site.register(Version, UniversalAdmin)