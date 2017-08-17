from django import forms

from .models import *


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            )
        }
