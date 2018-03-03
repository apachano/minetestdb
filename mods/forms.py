from django.forms import ModelForm
from .models import Mod


class NewModForm(ModelForm):

    class Meta:
        model = Mod
        fields = ['name', 'git', 'download', 'mt_version', 'description', 'tags']
        exclude = ['author']
