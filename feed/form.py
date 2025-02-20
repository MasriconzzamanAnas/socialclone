from django import forms
from . import models

class postform(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','text','catagory','img' ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'catagory': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
        }