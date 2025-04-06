from django import forms # type: ignore
from .models import CommandeAchat

class CommandeAchatForm(forms.ModelForm):
    class Meta:
        model = CommandeAchat
        fields = [
            'date_commande', 'statut', 'quantite_demandee',
            'prix', 'prix_total', 'fournisseur', 'remarques'
        ]
        widgets = {
            'date_commande': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'statut': forms.TextInput(attrs={'class': 'form-control'}),
            'quantite_demandee': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'prix_total': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'fournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'remarques': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        prix = cleaned_data.get("prix")
        quantite_demandee = cleaned_data.get("quantite_demandee")

        if prix is not None and quantite_demandee is not None:
            cleaned_data["prix_total"] = prix * quantite_demandee

        return cleaned_data


class ModifierPrixForm(forms.ModelForm):
    class Meta:
        model = CommandeAchat
        fields = ["prix"]
        widgets = {
            "prix": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"})
        }
        labels = {
            "prix": "Nouveau Prix (DA)"
        }
