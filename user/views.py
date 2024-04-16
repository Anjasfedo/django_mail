from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .forms import UserLoginForm, UserProfileForm

# Create your views here.


def user_login(request):
    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            remember_me = form.cleaned_data.get('remember_me')

            login(request, form.get_user())

            if not remember_me:
                # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
                request.session.set_expiry(0)

            return redirect('dashboard')

    context = {
        'form': form,
        'is_auth_page': True
    }

    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)

    return redirect('user_login')


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
