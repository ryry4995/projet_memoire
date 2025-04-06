from django import forms  # type: ignore
from .models import DemandeAchat, Article

class DemandeAchatForm(forms.ModelForm):
    class Meta:
        model = DemandeAchat
        fields = ['id_article', 'quantite_demandee', 'date_demande', 'statut', ]
        widgets = {
            'date_demande': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select a date'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Récupère le queryset des articles
        self.fields['id_article'].queryset = Article.objects.all()
        # Définit le label du champ
        self.fields['id_article'].label = "Code Article"
        # Utilise le champ 'code_article' pour l'affichage dans le select
        self.fields['id_article'].label_from_instance = lambda obj: obj.code_article

    
        
        
