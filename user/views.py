from django.shortcuts import render
from .forms import UserLoginForm

# Create your views here.

def login(request):
    context = {
        'form': UserLoginForm()
    }
    
    return render(request, 'login.html', context)