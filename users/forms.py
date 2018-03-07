from django import forms



class ChangeContactForm(forms.Form):
    github = forms.CharField(label='GitHub', max_length=50, required=False)
    irc = forms.CharField(label='IRC', max_length=50, required=False)
    discord = forms.CharField(label='Discord', max_length=50, required=False)
    skype = forms.CharField(label='skype', max_length=50, required=False)
    ingame = forms.CharField(label='Ingame', max_length=50, required=False)