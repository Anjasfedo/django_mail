from django.shortcuts import render
from .forms import AgendaForm, IncomingMailForm, OutgoingMailForm, IncomingDispositionForm, OutgoingDispositionForm
from .models import Agenda, IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition
# Create your views here.


def dashboard(request):
    context = {
        # 'forms': [AgendaForm(), IncomingMailForm(), OutgoingMailForm(), IncomingDispositionForm(), OutgoingDispositionForm()]
        'agendas':  Agenda.objects.all()
    }

    return render(request, 'dashboard.html', context)


def incoming_mail(request):
    context = {
        'form': IncomingMailForm(),
        'incoming_mails':  IncomingMail.objects.all()
    }

    return render(request, 'incoming_mail.html', context)


def outgoing_mail(request):
    context = {
        'form': OutgoingMailForm(),
        'outgoing_mails':  OutgoingMail.objects.all()
    }

    return render(request, 'outgoing_mail.html', context)


def incoming_disposition(request):
    context = {
        'form': IncomingDispositionForm(),
        'incoming_dispositions': IncomingDisposition.objects.all()
    }

    return render(request, 'incoming_disposition.html', context)


def outgoing_disposition(request):
    context = {
        'form': OutgoingDispositionForm(),
        'outgoing_dispositions': OutgoingDisposition.objects.all()
    }

    return render(request, 'outgoing_disposition.html', context)


def agenda(request):
    context = {
        'form': AgendaForm(),
        'agendas':  Agenda.objects.all()
    }

    return render(request, 'agenda.html', context)
