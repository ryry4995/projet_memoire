from django.urls import path # type: ignore
from . import views  # Importez les vues de l'application
from .views import supprimer_commande,modifier_prix
app_name = 'commande_achat'  # Déclarez le namespace de l'application

urlpatterns = [
    path('commandes/', views.commande_list, name='commande_list'), 
    path('commande/<int:id_commande>/', views.commande_detail, name='commande_detail'), 
    path('commande/<int:id_commande>/changer_statut/<str:nouveau_statut>/', views.changer_statut_commande, name='changer_statut_commande'), 
    path('commande/modifier/<int:id_commande>/', views.modifier_commande, name='modifier_commande'),
    path('commande/delete/<int:id_commande>/', views.supprimer_commande, name='supprimer_commande'),

    path("modifier_prix/<int:commande_id>/", modifier_prix, name="modifier_prix"),
      # Route pour la liste des commandes
    # Ajoutez d'autres routes si nécessaire, par exemple :
    # path('commandes/create/', views.commande_create, name='commande_create'),
]
