from django.urls import path # type: ignore
from .views import update_profile
from .views import profile_view
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
# profiles/urls.py

app_name = 'profiles'  # Cette ligne est indispensable

urlpatterns = [
    path('', profile_view, name='profile'),  # L'URL de base pour afficher le profil, ex: /profile/
    path('update/', update_profile, name='update_profile'),
]


urlpatterns = [
    # ... vos autres routes ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

