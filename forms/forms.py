from django import forms
from .models import *
from django.forms import widgets


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Signer
        exclude = ['user', ]
        fields = ('first name', 'last name', 'gender',
                  'languages', 'username', 'password')
