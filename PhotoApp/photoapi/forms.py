from dataclasses import field
from django import forms 
from .models import PhotoImageModel


class PhotoImageForm(forms.ModelForm):
    class Meta:
        model = PhotoImageModel
        fields = ('user_image',)