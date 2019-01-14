from django import forms
from .models import Neighbourhood, Profile ,Business


class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['user']