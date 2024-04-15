from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import AgendaForm, IncomingMailForm, OutgoingMailForm, IncomingDispositionCreateForm, IncomingDispositionUpdateForm, OutgoingDispositionCreateForm, OutgoingDispositionUpdateForm
from .models import Agenda, IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition
from .resources import IncomingMailResource, OutgoingMailResource, IncomingDispositionResource, OutgoingDispositionResource

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


def incoming_mail_export(request):
    incoming_mail_resources = IncomingMailResource()
    dataset = incoming_mail_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Incoming_mail.xls"'

    return response


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


def outgoing_mail_export(request):
    outgoing_mail_resources = OutgoingMailResource()
    dataset = outgoing_mail_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Outgoing_mail.xls"'

    return response


def incoming_disposition(request):
    form = IncomingDispositionCreateForm(request.user)

    if request.method == 'POST':
        form = IncomingDispositionCreateForm(request.user, request.POST)
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
    form = IncomingDispositionUpdateForm(
        request.user, instance=incoming_disposition)

    if request.method == 'POST':
        form = IncomingDispositionUpdateForm(request.user,
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


def incoming_disposition_export(request):
    incoming_disposition_resources = IncomingDispositionResource()
    dataset = incoming_disposition_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Incoming_disposition.xls"'

    return response


def outgoing_disposition(request):
    form = OutgoingDispositionCreateForm(request.user)

    if request.method == 'POST':
        form = OutgoingDispositionCreateForm(request.user, request.POST)
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
    form = OutgoingDispositionUpdateForm(request.user, instance=outgoing_disposition)
    form.helper.form_action = reverse_lazy(
        'outgoing_disposition_update', kwargs={'pk': outgoing_disposition.id})

    if request.method == 'POST':
        form = OutgoingDispositionUpdateForm(request.user,
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


def outgoing_disposition_export(request):
    outgoing_disposition_resources = OutgoingDispositionResource()
    dataset = outgoing_disposition_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Outgoing_disposition.xls"'

    return response


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
