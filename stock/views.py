from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.http import JsonResponse  # type: ignore
from django.contrib import messages  # type: ignore
from .models import Stock, Article
from .forms import StockForm, StockConsomerForm

# Liste des articles en stock
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, "stock/stock_list.html", {"stocks": stocks})

# Supprimer un article en stock
def stock_delete(request, code_article):
    stock = get_object_or_404(Stock, code_article=code_article)
    stock.delete()
    messages.success(request, "Article supprimé avec succès.")
    return redirect("stock:stock_list")

# Détails d’un article en stock
def stock_detail(request, code_article):
    article = get_object_or_404(Article, code_article=code_article)
    stock, created = Stock.objects.get_or_create(
        code_article=article.code_article, 
        defaults={"stock_consomer": 0, "stock_total": 0}
    )

    if request.method == "POST":
        form = StockConsomerForm(request.POST)
        if form.is_valid():
            stock_consomme = form.cleaned_data["stock_consomer"]
            stock.stock_consomer += stock_consomme  # Mise à jour du stock consommé
            stock.save()

            messages.success(request, "Stock consommé mis à jour avec succès !")
            return redirect("stock:stock_detail", code_article=code_article)
    else:
        form = StockConsomerForm()

    return render(request, "stock/stock_detail.html", {"article": article, "stock": stock, "form": form})

# Mise à jour du stock consommé
def stock_update(request, code_article):
    stock = get_object_or_404(Stock, code_article=code_article)

    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            new_stock_consomer = form.cleaned_data["stock_consomer"]

            if new_stock_consomer < 0:
                return JsonResponse({"error": "La quantité consommée ne peut pas être négative."}, status=400)

            stock.stock_consomer = new_stock_consomer
            stock.save()

            return JsonResponse({
                "message": "Stock mis à jour avec succès",
                "quantite_restante": stock.quantite_restante  # Utilisation de la propriété quantite_restante
            })

    else:
        form = StockForm(instance=stock)

    return render(request, "stock/stock_update.html", {"form": form, "stock": stock})
