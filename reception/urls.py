from django.urls import path # type: ignore
from .views import reception_list, reception_detail, change_statut_reception,supprimer_reception,modifier_quantite_reception
app_name = 'reception' 
urlpatterns = [
    path('', reception_list, name='reception_list'),
    path('<int:pk>/', reception_detail, name='reception_detail'),
    path('change_statut/<int:pk>/<str:statut>/', change_statut_reception, name='change_statut_reception'),
    path('supprimer/<int:pk>/', supprimer_reception, name='supprimer_reception'),
    path("modifier/<int:reception_id>/", modifier_quantite_reception, name="modifier_quantite_reception"),

]
