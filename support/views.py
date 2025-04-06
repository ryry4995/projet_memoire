from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from .forms import ContactForm
from .models import SupportMessage  # Assure-toi que c'est bien importé

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde les données dans la BDD
            messages.success(request, "Votre message a été envoyé avec succès !")
            return redirect('contact')  # Rediriger pour éviter le re-submit
    else:
        form = ContactForm()
    
    return render(request, 'support/contact.html', {'form': form})

