from django.shortcuts import render
from .forms import *
# Create your views here.


def dashboard(request):
    context = {
        'forms': [AgendaForm(), IncomingMailForm(), OutgoingMailForm(), IncomingDispositionForm(), OutgoingDispositionForm()]
    }

    return render(request, 'dashboard.html', context)
