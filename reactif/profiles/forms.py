from django import forms # type: ignore
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'bio']  # Ajoutez d'autres champs si nécessaire
