from django.shortcuts import render, get_object_or_404, redirect  # type: ignore
from django.http import JsonResponse  # type: ignore
from .models import Reception
from stock.models import Stock
import json
from urllib.parse import unquote

def modifier_quantite_reception(request, reception_id):
    print(f"🔹 Requête reçue pour modifier la réception {reception_id}")

    if request.method == "POST":
        try:
            # Charger les données JSON envoyées
            data = json.loads(request.body)
            print(f"🔹 Données reçues : {data}")  # Log pour vérifier les données reçues

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

            print(f"✅ Quantité mise à jour avec succès ! Quantité totale : {reception.quantite_receptionnee}")
            return JsonResponse({"success": True})

        except Exception as e:
            print(f"❌ Erreur: {str(e)}")
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    print("❌ Méthode non autorisée")
    return JsonResponse({"success": False, "error": "Méthode non autorisée"}, status=405)



def change_statut_reception(request, pk, statut):
    try:
        reception = get_object_or_404(Reception, pk=pk)

        if reception.quantite_receptionnee is None:
            reception.quantite_receptionnee = 0

        reception.statut = statut
        reception.save()

        if statut == "Réceptionné":
            # 🔁 Recalcule le stock total pour TOUTES les réceptions de ce code_article
            receptions = Reception.objects.filter(code_article=reception.code_article, statut="Réceptionné")

            stock_total_ajoute = sum(
                r.quantite_receptionnee * r.quantite_unitaire
                for r in receptions
                if r.quantite_receptionnee and r.quantite_unitaire
            )

            # Met à jour ou crée le stock
            stock, created = Stock.objects.get_or_create(
                code_article=reception.code_article,
                defaults={
                    "designation": reception.designation,
                    "unite": reception.unite,
                    "quantite_demandee": 0,
                    "stock_consomer": 0,
                    "stock_total": stock_total_ajoute,
                    "id_reception": reception,
                },
            )

            if not created:
                stock.stock_total = stock_total_ajoute
                stock.save()

            print("✅ Stock mis à jour (recalcul global).")
            return redirect("stock:stock_list")

        return redirect("reception:reception_list")

    except Exception as e:
        print(f"❌ Erreur: {str(e)}")
        return JsonResponse({"success": False, "error": str(e)}, status=500)

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
