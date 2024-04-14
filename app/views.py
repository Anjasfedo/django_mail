from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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
    form = IncomingMailForm()

    if request.method == 'POST':
        form = IncomingMailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('incoming_mail')

    context = {
        'form': form,
        'incoming_mails':  IncomingMail.objects.all()
    }

    return render(request, 'incoming_mail.html', context)


def incoming_mail_update(request, pk):
    incoming_mail = IncomingMail.objects.get(id=pk)
    form = IncomingMailForm(instance=incoming_mail)

    if request.method == 'POST':
        form = IncomingMailForm(
            request.POST, request.FILES, instance=incoming_mail)
        if form.is_valid():
            form.save()
            return redirect('incoming_mail')

    context = {
        'form': form,
    }

    return render(request, 'incoming_mail_update.html', context)


def outgoing_mail(request):
    form = OutgoingMailForm()

    if request.method == 'POST':
        form = OutgoingMailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('outgoing_mail')

    context = {
        'form': form,
        'outgoing_mails':  OutgoingMail.objects.all()
    }

    return render(request, 'outgoing_mail.html', context)


def incoming_disposition(request):
    form = IncomingDispositionForm()

    if request.method == 'POST':
        form = IncomingDispositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incoming_disposition')

    context = {
        'form': form,
        'incoming_dispositions': IncomingDisposition.objects.all()
    }

    return render(request, 'incoming_disposition.html', context)


def outgoing_disposition(request):
    form = OutgoingDispositionForm()

    if request.method == 'POST':
        form = OutgoingDispositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outgoing_disposition')

    context = {
        'form': form,
        'outgoing_dispositions': OutgoingDisposition.objects.all()
    }

    return render(request, 'outgoing_disposition.html', context)


def agenda(request):
    form = AgendaForm()

    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agenda')

    context = {
        'form': form,
        'agendas':  Agenda.objects.all()
    }

    return render(request, 'agenda.html', context)


def agenda_update(request, pk):
    agenda = Agenda.objects.get(id=pk)
    form = AgendaForm(instance=agenda)
    form.helper.form_action = reverse_lazy('agenda_update', kwargs={'pk': agenda.id})

    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            return redirect('agenda')

    context = {
        'form': form,
    }

    return render(request, 'agenda_update.html', context)

def agenda_delete(request, pk):
    agenda = Agenda.objects.get(id=pk)
    print(agenda)

    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda')

    return redirect('agenda')