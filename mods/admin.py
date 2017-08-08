from django.contrib import admin

from .models import Mod
from .models import Tag


class ModAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')


admin.site.register(Mod, ModAdmin)
admin.site.register(Tag)