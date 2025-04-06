from django import forms # type: ignore
from .models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'code_article', 'designation', 'categorie', 
            'unite', 'date_expiration', 'status' ,'quantite_unitaire',
        ]
        widgets = {
            'date_expiration': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(choices=[('actif', 'Actif'), ('elaboration', 'elaboration')]),
        }

    def clean(self):
        cleaned_data = super().clean()
        quantite_demandee = cleaned_data.get('quantite_demandee')
        prix = cleaned_data.get('prix')
        
        if quantite_demandee and prix:
            prix_total = quantite_demandee * prix
            cleaned_data['prix_total'] = prix_total  # Calcul et assignation du prix total
            
        return cleaned_data