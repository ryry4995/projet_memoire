from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import DemandeAchat
from .forms import DemandeAchatForm

def home(request):
    """
    Vue pour afficher la page d'accueil.
    """
    return render(request, 'home.html')

def demande_achat_list(request):
    demandes = DemandeAchat.objects.all()
    return render(request, 'demande_achat/demande_achat_list.html', {'demandes': demandes})



def demande_achat_create(request):
    if request.method == 'POST':
        form = DemandeAchatForm(request.POST)
        if form.is_valid():
            # Création sans enregistrer immédiatement en base
            demande = form.save(commit=False)
            # Forcer le statut à 'en_attente' lors de la création
            demande.statut = 'en_attente'
            demande.save()
            # Redirection vers la page de détail (à adapter selon vos URLs)
            return redirect('demande_achat:demande_achat_list')
    else:
        form = DemandeAchatForm()

    return render(request, 'demande_achat/demande_achat_create.html', {'form': form})

def demande_achat_edit(request, pk):
    """
    Vue pour modifier une demande d'achat existante.
    """
    demande = get_object_or_404(DemandeAchat, pk=pk)  # Récupère la demande ou lève une erreur 404

    if request.method == 'POST':
        form = DemandeAchatForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('demande_achat:demande_achat_list')
    else:
        form = DemandeAchatForm(instance=demande)  # Pré-remplit le formulaire avec les données existantes

    return render(request, 'demande_achat/demande_achat_form.html', {'form': form})

def demande_achat_delete(request, pk):
    """
    Vue pour supprimer une demande d'achat existante.
    """
    demande = get_object_or_404(DemandeAchat, pk=pk)  # Récupère la demande ou lève une erreur 404

    if request.method == 'POST':
        demande.delete()
        return redirect('demande_achat:demande_achat_list')  # Redirige après la suppression

    return render(request, 'demande_achat/demande_achat_confirm_delete.html', {'demande': demande})
# Dans demande_achat/views.py


def approve_demande(request, demande_id):
    # Récupérer la demande d'achat à partir de l'ID
    demande = get_object_or_404(DemandeAchat, pk=demande_id)
    
    # Vérifier que le statut est "en attente" et qu'il n'a pas déjà été approuvé
    if demande.statut != 'approuve':
        demande.statut = 'approuve'
        demande.save()

        # Créer la commande d'achat pour la demande approuvée
        demande.create_commande()

        return redirect('demande_achat:demande_achat_list')  # Rediriger vers la liste des demandes d'achat
    else:
        # Si la demande est déjà approuvée, vous pouvez gérer un message ou une autre action
        return redirect('demande_achat:demande_achat_list')
