from django.shortcuts import render
from .forms import *
# Create your views here.


def dashboard(request):
    context = {
        'forms': [AgendaForm(), IncomingMailForm(), OutgoingMailForm(), IncomingDispositionForm(), OutgoingDispositionForm()]
    }

    return render(request, 'dashboard.html', context)


def incoming_mail(request):
    context = {
        'form': IncomingMailForm()
    }

    return render(request, 'incoming_mail.html', context)


def outgoing_mail(request):
    context = {
        'form': OutgoingMailForm()
    }

    return render(request, 'outgoing_mail.html', context)


def incoming_disposition(request):
    context = {
        'form': IncomingDispositionForm()
    }

    return render(request, 'incoming_disposition.html', context)


def outgoing_disposition(request):
    context = {
        'form': OutgoingDispositionForm()
    }

    return render(request, 'outgoing_disposition.html', context)


def agenda(request):
    context = {
        'form': AgendaForm()
    }

    return render(request, 'agenda.html', context)
