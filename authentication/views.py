# authentication/views.py
from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth import login, logout, authenticate # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.http import HttpResponseRedirect # type: ignore

# Vue pour la page d'accueil après connexion
def home_view(request):
    return render(request, 'registration/home.html')

# Vue pour la page de connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue {user.username}! Vous êtes maintenant connecté.")
            return redirect('article:home_view')
        else:
            messages.error(request, "Identifiant ou mot de passe incorrect. Veuillez réessayer.")
    
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Vue pour la déconnexion
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('authentication:login')  # Redirige vers la page de login après déconnexion
    else:
        return redirect('article:home_view')  # Si accès direct à la vue via GET, rediriger vers l'accueil

# Vue pour l'inscription
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Compte créé pour {username}. Vous pouvez maintenant vous connecter.")
            return redirect('authentication:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erreur dans le champ '{field}': {error}")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
