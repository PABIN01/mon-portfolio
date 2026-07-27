# Forms for the contact app
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Votre nom complet',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'votre@email.com',
                'class': 'form-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Sujet de votre message',
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Décrivez votre projet ou demande...',
                'class': 'form-input',
                'rows': 6,
            }),
        }
