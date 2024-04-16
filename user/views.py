from django.shortcuts import render, redirect
from .forms import UserProfileForm

# Create your views here.


def user_profile_update(request):
    user = request.user
    form = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_profile_update')

    context = {
        'form': form
    }

    return render(request, 'user_profile_update.html', context)
