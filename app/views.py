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
    form = IncomingMailForm(request.user)

    if request.method == 'POST':
        form = IncomingMailForm(request.user, request.POST, request.FILES)
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
    form = IncomingMailForm(request.user, instance=incoming_mail)
    form.helper.form_action = reverse_lazy(
        'incoming_mail_update', kwargs={'pk': incoming_mail.id})

    if request.method == 'POST':
        form = IncomingMailForm(request.user,
                                request.POST, request.FILES, instance=incoming_mail)
        if form.is_valid():
            form.save()
            return redirect('incoming_mail')

    context = {
        'form': form,
    }

    return render(request, 'incoming_mail_update.html', context)


def incoming_mail_delete(request, pk):
    incoming_mail = IncomingMail.objects.get(id=pk)

    if request.method == 'POST':
        incoming_mail.delete()
        return redirect('incoming_mail')

    return redirect('incoming_mail')


def outgoing_mail(request):
    form = OutgoingMailForm(request.user)

    if request.method == 'POST':
        form = OutgoingMailForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('outgoing_mail')

    context = {
        'form': form,
        'outgoing_mails':  OutgoingMail.objects.all()
    }

    return render(request, 'outgoing_mail.html', context)


def outgoing_mail_update(request, pk):
    outgoing_mail = OutgoingMail.objects.get(id=pk)
    form = OutgoingMailForm(request.user, instance=outgoing_mail)
    form.helper.form_action = reverse_lazy(
        'outgoing_mail_update', kwargs={'pk': outgoing_mail.id})

    if request.method == 'POST':
        form = OutgoingMailForm(request.user,
                                request.POST, request.FILES, instance=outgoing_mail)
        if form.is_valid():
            form.save()
            return redirect('outgoing_mail')

    context = {
        'form': form,
    }

    return render(request, 'outgoing_mail_update.html', context)


def outgoing_mail_delete(request, pk):
    outgoing_mail = OutgoingMail.objects.get(id=pk)

    if request.method == 'POST':
        outgoing_mail.delete()
        return redirect('outgoing_mail')

    return redirect('outgoing_mail')


def incoming_disposition(request):
    form = IncomingDispositionForm(request.user)

    if request.method == 'POST':
        form = IncomingDispositionForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('incoming_disposition')

    context = {
        'form': form,
        'incoming_dispositions': IncomingDisposition.objects.all()
    }

    return render(request, 'incoming_disposition.html', context)


def incoming_disposition_update(request, pk):
    incoming_disposition = IncomingDisposition.objects.get(id=pk)
    form = IncomingDispositionForm(request.user, instance=incoming_disposition)
    form.helper.form_action = reverse_lazy(
        'incoming_disposition_update', kwargs={'pk': incoming_disposition.id})

    if request.method == 'POST':
        form = IncomingDispositionForm(request.user,
                                       request.POST, instance=incoming_disposition)
        if form.is_valid():
            form.save()
            return redirect('incoming_disposition')

    context = {
        'form': form,
    }

    return render(request, 'incoming_disposition_update.html', context)


def incoming_disposition_delete(request, pk):
    incoming_disposition = IncomingDisposition.objects.get(id=pk)

    if request.method == 'POST':
        incoming_disposition.delete()
        return redirect('incoming_disposition')

    return redirect('incoming_disposition')


def outgoing_disposition(request):
    form = OutgoingDispositionForm(request.user)

    if request.method == 'POST':
        form = OutgoingDispositionForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('outgoing_disposition')

    context = {
        'form': form,
        'outgoing_dispositions': OutgoingDisposition.objects.all()
    }

    return render(request, 'outgoing_disposition.html', context)


def outgoing_disposition_update(request, pk):
    outgoing_disposition = OutgoingDisposition.objects.get(id=pk)
    form = OutgoingDispositionForm(request.user, instance=outgoing_disposition)
    form.helper.form_action = reverse_lazy(
        'outgoing_disposition_update', kwargs={'pk': outgoing_disposition.id})

    if request.method == 'POST':
        form = OutgoingDispositionForm(request.user,
                                       request.POST, instance=outgoing_disposition)
        if form.is_valid():
            form.save()
            return redirect('outgoing_disposition')

    context = {
        'form': form,
    }

    return render(request, 'outgoing_disposition_update.html', context)


def outgoing_disposition_delete(request, pk):
    outgoing_disposition = OutgoingDisposition.objects.get(id=pk)

    if request.method == 'POST':
        outgoing_disposition.delete()
        return redirect('outgoing_disposition')

    return redirect('outgoing_disposition')


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
    form.helper.form_action = reverse_lazy(
        'agenda_update', kwargs={'pk': agenda.id})

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

    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda')

    return redirect('agenda')
