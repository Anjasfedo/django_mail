from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import logout, login

# Create your views here.

def user_login(request):
    form = UserLoginForm()
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    
    context = {
        'form': form,
        'is_auth_page': True
    }
    
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)

    return redirect('user_login')