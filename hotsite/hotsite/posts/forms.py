from django import forms

from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'thumbnail']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
