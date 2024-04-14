from django.shortcuts import render
from .forms import *

# Create your views here.


def dashboard(request):
    context = {
        
    }

    return render(request, 'dashboard.html', context)
