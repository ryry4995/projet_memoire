from django.apps import AppConfig # type: ignore

class ReceptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reception'  # ✅ Tout en minuscules
