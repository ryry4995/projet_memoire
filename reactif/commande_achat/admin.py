from django.contrib import admin # type: ignore
from .models import CommandeAchat

class CommandeAchatAdmin(admin.ModelAdmin):
    list_display = ('id_commande', 'date_commande', 'prix', 'quantite_demandee', 'prix_total')
    search_fields = ('fournisseur',)

admin.site.register(CommandeAchat, CommandeAchatAdmin)

# Register your models here.
