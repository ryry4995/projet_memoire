from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Article
from .forms import ArticleForm
from django.contrib import messages # type: ignore
from django.db.models import Q # type: ignore
from datetime import datetime
from stock.models import Stock

def low_stock(request):
    # Récupérer les articles en stock faible
    articles = Article.objects.filter(stock__lt=10)  # Par exemple
    return render(request, 'article/low_stock.html', {'articles': articles})
def home_view(request):
    # Récupérer tous les stocks
    stocks = Stock.objects.all()

    # Créer une liste des stocks bas sous forme de dictionnaires
    stock_bas = [
        {
            "designation": stock.designation,
            "code_article": stock.code_article,
            "quantite_restante": (stock.stock_total or 0) - (stock.stock_consomer or 0)
        }
        for stock in stocks if ((stock.stock_total or 0) - (stock.stock_consomer or 0)) <= 2000
    ]

    # Renvoyer les données à la vue
    return render(request, 'home.html', {'stock_bas': stock_bas})


def search_view(request):
    query = request.GET.get('q', '')
    if query:
        results = Article.objects.filter(
            Q(code_article__icontains=query) |
            Q(designation__icontains=query) |
            Q(categorie__icontains=query) |
            Q(unite__icontains=query)
        )
    else:
        results = Article.objects.none()  # Aucun résultat si la requête est vide

    return render(request, 'article/search_results.html', {'query': query, 'results': results})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Utilisez 'article/article_detail.html' si votre template est dans article/templates/article/
    return render(request, 'article/article_detail.html', {'article': article})
def article_list(request):
    context = {
        'articles': Article.objects.all(),
        
    }
    return render(request, 'article/article_list.html', context)


def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article:article_list')
    else:
        form = ArticleForm()
    
    context = {
        'form': form,
        'article': None  # Aucune ID pour la création
    }
    return render(request, 'article/article_form.html', context)


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article:article_list')
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article
    }
    return render(request, 'article/article_form.html', context)

def article_delete(request, pk):
    # Récupération de l'article ou renvoie une erreur 404 si l'article n'existe pas
    article = get_object_or_404(Article, id_article=pk)

    if request.method == 'POST':
        article.delete()
        # Message après la suppression réussie
        messages.success(request, 'L\'article a été supprimé avec succès.')
        return redirect('article:article_list')

    # Afficher le formulaire de confirmation
    context = {'article': article}
    return render(request, 'article/article_delete.html', context)