from django import forms
from .models import Blog, Work, Category, Tag, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'contact', 'message']
