# demande_achat/urls.py
from django.urls import path # type: ignore
from . import views

# demande_achat/urls.py
app_name = 'demande_achat'

urlpatterns = [
    path('', views.home, name='home'),
    path('demande_achat_list', views.demande_achat_list, name='demande_achat_list'),
    path('create/', views.demande_achat_create, name='demande_achat_create'),
    path('approve/<int:demande_id>/', views.approve_demande, name='approve_demande'),
    path('edit/<int:pk>/', views.demande_achat_edit, name='demande_achat_edit'),
    path('delete/<int:pk>/', views.demande_achat_delete, name='demande_achat_delete'),
]

