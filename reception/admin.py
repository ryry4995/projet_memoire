from django.contrib import admin # type: ignore
from .models import Reception

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('id_reception', 'code_article', 'designation', 'quantite_receptionnee', 'unite', 'statut')
    search_fields = ('code_article', 'designation')
    list_filter = ('statut',)

admin.site.register(Reception, ReceptionAdmin)


