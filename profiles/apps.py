
from django.apps import AppConfig # type: ignore

class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import profiles.signals  # Cet import active les signaux dès le démarrage de l'app


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
