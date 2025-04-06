from django import forms # type: ignore
from .models import Stock, Article

# Formulaire pour gérer l'ajout et la mise à jour du stock
class StockForm(forms.ModelForm):
    code_article = forms.ModelChoiceField(
        queryset=Article.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Sélectionnez un article",
        label="Code Article"
    )

    class Meta:
        model = Stock
        fields = ["code_article", "stock_consomer"]
        widgets = {
            "stock_consomer": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }

# Formulaire pour ajouter une consommation de stock
class StockConsomerForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["stock_consomer"]
        widgets = {
            "stock_consomer": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }
