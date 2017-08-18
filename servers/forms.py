from django.forms import ModelForm

from .models import Server


class NewServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'address', 'website', 'description', 'mt_version', 'tags']
        exclude = ['owner']