from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import ProfileForm


@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html', {'user': request.user})
@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige vers une page de visualisation de profil par exemple
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_update.html', {'form': form})
