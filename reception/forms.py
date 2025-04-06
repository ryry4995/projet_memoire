from django import forms # type: ignore
from .models import Reception


class ModifierQuantiteReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ["quantite_receptionnee"]
        widgets = {
            "quantite_receptionnee": forms.NumberInput(attrs={"class": "form-control", "min": "0"})
        }
        labels = {
            "quantite_receptionnee": "Quantité réceptionnée"
        }
