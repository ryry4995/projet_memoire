from django import forms # type: ignore
from .models import SupportMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['email', 'sujet', 'message']
