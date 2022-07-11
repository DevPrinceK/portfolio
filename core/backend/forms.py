from django import forms
from .models import Blog, Work, Category, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'contact', 'message']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['author', 'date', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', }),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
