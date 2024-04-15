from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import logout, login

# Create your views here.

def user_login(request):
    form = UserLoginForm()
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        
        if form.is_valid():
            remember_me = form.cleaned_data.get('remember_me')
            
            login(request, form.get_user())
            
            if not remember_me:
                    request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
            
            return redirect('dashboard')
    
    context = {
        'form': form,
        'is_auth_page': True
    }
    
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)

    return redirect('user_login')