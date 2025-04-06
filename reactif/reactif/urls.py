from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.shortcuts import redirect # type: ignore
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    path('', lambda request: redirect('accounts/login/')),  # Redirige vers la page de connexion
    path('accounts/', include('authentication.urls')),  # Inclut les URLs de l'application authentication
    path('admin/', admin.site.urls),  # Route pour l'admin
    path('article/', include('article.urls')),  # Inclut les URLs de l'application article
    path('demande-achat/', include('demande_achat.urls')),
    path('commande-achat/', include('commande_achat.urls')),
    path("reception/", include("reception.urls")),
    path("stock/", include("stock.urls")),
    path('support/', include('support.urls')),
]

