from django import forms
from .models import Appteste

class ApptesteForm(forms.ModelForm):
    class Meta:
        model = Appteste
        fields = ['description', 'price', 'quantity']