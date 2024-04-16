from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.conf import settings
# from django.views.decorators.cache import cache_page
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models.functions import ExtractWeekDay
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from .forms import AgendaForm, IncomingMailForm, OutgoingMailForm, IncomingDispositionCreateForm, IncomingDispositionUpdateForm, OutgoingDispositionCreateForm, OutgoingDispositionUpdateForm, UserProfileForm
from .models import Agenda, IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition
from .resources import IncomingMailResource, OutgoingMailResource, IncomingDispositionResource, OutgoingDispositionResource, IncomingAgendaDetailResource, OutgoingAgendaDetailResource
import datetime

# Cache Setup
# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.

@login_required
# @cache_page(CACHE_TTL)
def dashboard(request):
    current_year = datetime.date.today().year
    today = timezone.now().date()
    start_of_week = today - timezone.timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)

    # Data for the chart - Incoming mails by day of the week
    incoming_mails_by_day = IncomingMail.objects.filter(
        date__year=current_year
    ).annotate(
        day_of_week=ExtractWeekDay('date')
    ).values(
        'day_of_week'
    ).annotate(
        mail_count=Count('id')
    )

    # Data for the chart - Outgoing mails by day of the week
    outgoing_mails_by_day = OutgoingMail.objects.filter(
        date__year=current_year
    ).annotate(
        day_of_week=ExtractWeekDay('date')
    ).values(
        'day_of_week'
    ).annotate(
        mail_count=Count('id')
    )

    # Combine the incoming and outgoing mails into one queryset
    combined_mails_by_day = incoming_mails_by_day.union(outgoing_mails_by_day)

    # Aggregate the counts for each day of the week
    aggregated_data = {}
    for entry in combined_mails_by_day:
        day_of_week = entry['day_of_week']
        mail_count = entry['mail_count']
        if day_of_week not in aggregated_data:
            aggregated_data[day_of_week] = mail_count
        else:
            aggregated_data[day_of_week] += mail_count

    # Sort the aggregated data by day of the week
    sorted_data = sorted(aggregated_data.items(), key=lambda x: x[0])

    # Prepare data for the chart
    labels = ['Sunday', 'Monday', 'Tuesday',
              'Wednesday', 'Thursday', 'Friday', 'Saturday']
    data = [entry[1] for entry in sorted_data]

    # Calculate total mails for today
    total_mails_today = IncomingMail.objects.filter(
        date=today).count() + OutgoingMail.objects.filter(date=today).count()

    # Calculate total mails for this week
    total_mails_this_week = IncomingMail.objects.filter(date__gte=start_of_week).count(
    ) + OutgoingMail.objects.filter(date__gte=start_of_week).count()

    # Calculate total mails for this month
    total_mails_this_month = IncomingMail.objects.filter(date__gte=start_of_month).count(
    ) + OutgoingMail.objects.filter(date__gte=start_of_month).count()

    # Calculate total mails for this year
    total_mails_this_year = IncomingMail.objects.filter(date__year=current_year).count(
    ) + OutgoingMail.objects.filter(date__year=current_year).count()

    context = {
        'users': User.objects.all(),
        'total_incoming_mail': IncomingMail.objects.count(),
        'total_outgoing_mail': OutgoingMail.objects.count(),
        'total_incoming_disposition': IncomingDisposition.objects.count(),
        'total_outgoing_disposition': OutgoingDisposition.objects.count(),
        'current_year': current_year,
        'labels': labels,
        'data': data,
        'total_mails_today': total_mails_today,
        'total_mails_this_week': total_mails_this_week,
        'total_mails_this_month': total_mails_this_month,
        'total_mails_this_year': total_mails_this_year,
    }

    return render(request, 'dashboard.html', context)

@login_required
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

@login_required
def incoming_mail_update(request, pk):
    incoming_mail = get_object_or_404(IncomingMail, pk=pk)
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

@login_required
def incoming_mail_delete(request, pk):
    incoming_mail = get_object_or_404(IncomingMail, pk=pk)

    if request.method == 'POST':
        incoming_mail.delete()
        return redirect('incoming_mail')

    return redirect('incoming_mail')

@login_required
def incoming_mail_export(request):
    incoming_mail_resources = IncomingMailResource()
    dataset = incoming_mail_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Incoming_mail.xls"'

    return response

@login_required
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

@login_required
def outgoing_mail_update(request, pk):
    outgoing_mail = get_object_or_404(OutgoingMail, pk=pk)
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

@login_required
def outgoing_mail_delete(request, pk):
    outgoing_mail = get_object_or_404(OutgoingMail, pk=pk)

    if request.method == 'POST':
        outgoing_mail.delete()
        return redirect('outgoing_mail')

    return redirect('outgoing_mail')

@login_required
def outgoing_mail_export(request):
    outgoing_mail_resources = OutgoingMailResource()
    dataset = outgoing_mail_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Outgoing_mail.xls"'

    return response

@login_required
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

@login_required
def incoming_disposition_update(request, pk):
    incoming_disposition = get_object_or_404(IncomingDisposition, pk=pk)
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

@login_required
def incoming_disposition_delete(request, pk):
    incoming_disposition = get_object_or_404(IncomingDisposition, pk=pk)

    if request.method == 'POST':
        incoming_disposition.delete()
        return redirect('incoming_disposition')

    return redirect('incoming_disposition')

@login_required
def incoming_disposition_export(request):
    incoming_disposition_resources = IncomingDispositionResource()
    dataset = incoming_disposition_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Incoming_disposition.xls"'

    return response

@login_required
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

@login_required
def outgoing_disposition_update(request, pk):
    outgoing_disposition = get_object_or_404(OutgoingDisposition, pk=pk)
    form = OutgoingDispositionUpdateForm(
        request.user, instance=outgoing_disposition)
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

@login_required
def outgoing_disposition_delete(request, pk):
    outgoing_disposition = get_object_or_404(OutgoingDisposition, pk=pk)

    if request.method == 'POST':
        outgoing_disposition.delete()
        return redirect('outgoing_disposition')

    return redirect('outgoing_disposition')

@login_required
def outgoing_disposition_export(request):
    outgoing_disposition_resources = OutgoingDispositionResource()
    dataset = outgoing_disposition_resources.export()

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Outgoing_disposition.xls"'

    return response

@login_required
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

@login_required
def agenda_detail(request, pk):
    incoming_mails = IncomingMail.objects.filter(agenda_id=pk)
    incoming_dispositions = IncomingDisposition.objects.filter(
        mail__agenda_id=pk)

    outgoing_mails = OutgoingMail.objects.filter(agenda_id=pk)
    outgoing_dispositions = OutgoingDisposition.objects.filter(
        mail__agenda_id=pk)

    context = {
        'incoming_datas': zip(incoming_mails, incoming_dispositions),
        'outgoing_datas': zip(outgoing_mails, outgoing_dispositions),
        'pk': pk
    }

    return render(request, 'agenda_detail.html', context)

@login_required
def agenda_detail_incoming_export(request, pk):
    incoming_mails = IncomingMail.objects.filter(agenda_id=pk)
    incoming_dispositions = IncomingDisposition.objects.filter(
        mail__agenda_id=pk)

    # Zip incoming mails and dispositions
    incoming_data = zip(incoming_mails, incoming_dispositions)

    # Create an instance of the resource with incoming data
    resource = IncomingAgendaDetailResource()
    dataset = resource.export(queryset=incoming_data)

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="incoming_agenda_detail.xls"'

    return response

@login_required
def agenda_detail_outgoing_export(request, pk):
    outgoing_mails = OutgoingMail.objects.filter(agenda_id=pk)
    outgoing_dispositions = OutgoingDisposition.objects.filter(
        mail__agenda_id=pk)

    # Zip outgoing mails and dispositions
    outgoing_data = zip(outgoing_mails, outgoing_dispositions)

    # Create an instance of the resource with outgoing data
    resource = OutgoingAgendaDetailResource()
    dataset = resource.export(queryset=outgoing_data)

    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="outgoing_agenda_detail.xls"'

    return response

@login_required
def agenda_delete(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)

    if request.method == 'POST':
        agenda.delete()
        return redirect('agenda')

    return redirect('agenda')


@login_required
def user_profile_update(request):
    user = request.user
    form = UserProfileForm(instance=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('user_profile_update')

    context = {
        'form': form
    }

    return render(request, 'user_profile_update.html', context)