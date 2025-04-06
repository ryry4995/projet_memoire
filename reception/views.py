from django.shortcuts import render, get_object_or_404, redirect  # type: ignore
from django.http import JsonResponse  # type: ignore
from .models import Reception
from stock.models import Stock
import json


def modifier_quantite_reception(request, reception_id):
    print(f"🔹 Requête reçue pour modifier la réception {reception_id}")

    if request.method == "POST":
        try:
            # Charger les données JSON envoyées
            data = json.loads(request.body)
            nouvelle_quantite = data.get("quantite_receptionnee")

            # Conversion explicite de la quantité en entier si nécessaire
            if isinstance(nouvelle_quantite, str):
                nouvelle_quantite = int(nouvelle_quantite)

            # Vérification de la validité de la quantité reçue
            if nouvelle_quantite is None or nouvelle_quantite <= 0:
                return JsonResponse({"success": False, "error": "La quantité doit être un nombre positif"}, status=400)

            print(f"🔹 Nouvelle quantité reçue: {nouvelle_quantite}")

            # Récupérer la réception et vérifier si elle existe
            reception = get_object_or_404(Reception, id_reception=reception_id)

            # Vérification si la quantité réceptionnée est None et initialisation si nécessaire
            if reception.quantite_receptionnee is None:
                reception.quantite_receptionnee = 0

            # Mettre à jour la quantité réceptionnée dans la réception
            reception.quantite_receptionnee += nouvelle_quantite
            reception.save()

            print(f"✅ Quantité mise à jour avec succès !")
            return JsonResponse({"success": True})

        except Exception as e:
            print(f"❌ Erreur: {str(e)}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    print("❌ Méthode non autorisée")
    return JsonResponse({"success": False, "error": "Méthode non autorisée"}, status=405)



def change_statut_reception(request, pk, statut):
    # Récupérer la réception correspondant à l'ID
    reception = get_object_or_404(Reception, pk=pk)
    
    # Mettre à jour le statut de la réception
    reception.statut = statut
    reception.save()

    # Vérifier si le statut est "Réceptionné"
    if statut == "Réceptionné":
        # Rediriger vers la vue de stock (ajuster l'URL selon ta configuration)
        return redirect('stock:stock_list')  # Remplace 'stock:stock_list' par le nom de l'URL de la vue stock
    else:
        # Sinon, rediriger vers la liste des réceptions
        return redirect('reception:reception_list')
 # Redirige vers la liste des réceptions

def reception_detail(request, pk):
    reception = get_object_or_404(Reception, pk=pk)
    return render(request, 'reception/reception_detail.html', {'reception': reception})

def supprimer_reception(request, pk):
    reception = get_object_or_404(Reception, pk=pk)
    reception.delete()
    return redirect('reception:reception_list')  # Redirige vers la liste des réceptions


def reception_list(request):
    receptions = Reception.objects.all()
    return render(request, 'reception/reception_list.html', {'receptions': receptions})
