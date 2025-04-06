# Dans commande_achat/views.py
from django.contrib import messages # type: ignore
from django.shortcuts import render, redirect ,get_object_or_404# type: ignore
from django.http import HttpResponse # type: ignore
from .models import CommandeAchat
from .forms import CommandeAchatForm  # Assure-toi d’avoir un formulaire
import logging
from django.http import JsonResponse # type: ignore
from django.views.decorators.csrf import csrf_exempt # type: ignore
import json



logger = logging.getLogger(__name__)  # Pour enregistrer les erreurs dans les logs




def commande_list(request):
    commandes = CommandeAchat.objects.all()  # Liste de toutes les commandes
    return render(request, 'commande_achat/commande_list.html', {'commandes': commandes})

def commande_detail(request, id_commande):
    commande = CommandeAchat.objects.get(id_commande=id_commande)
    return render(request, 'commande_achat/commande_detail.html', {'commande': commande})

def supprimer_commande(request, id_commande):
    try:
        commande = CommandeAchat.objects.get(id_commande=id_commande)
        commande.delete()
        return JsonResponse({"success": True})
    except CommandeAchat.DoesNotExist:
        return JsonResponse({"error": "Commande non trouvée"}, status=404)
@csrf_exempt
def modifier_prix(request, commande_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            nouveau_prix = float(data.get("prix"))

            commande = CommandeAchat.objects.get(id_commande=commande_id)
            commande.prix = nouveau_prix
            commande.prix_total = commande.quantite_demandee * nouveau_prix
            commande.save()

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Méthode non autorisée"})
def modifier_commande(request, id_commande):
    commande = get_object_or_404(CommandeAchat, id_commande=id_commande)

    if request.method == "POST":
        form = CommandeAchatForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('commande_achat:commande_detail', id_commande=id_commande)

    else:
        form = CommandeAchatForm(instance=commande)

    return render(request, 'commande_achat/modifier_commande.html', {'form': form, 'commande': commande})

def changer_statut_commande(request, id_commande, nouveau_statut):
    try:
        commande = CommandeAchat.objects.get(id_commande=id_commande)
        commande.statut = nouveau_statut
        commande.save()
        return redirect('commande_achat:commande_list')  # Redirige vers la liste des commandes après modification
    except CommandeAchat.DoesNotExist:
        return HttpResponse("Commande non trouvée", status=404)