from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Ваше имя',
            'email': 'Электронная почта',
            'message': 'Сообщение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение'}),
        }
