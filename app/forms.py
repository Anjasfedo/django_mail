from django import forms
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Agenda, IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition
import datetime
from datetime import datetime as dt

# Utils Function


def year_choices():
    return [(r, r) for r in range(2000, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year

# Forms Classes


class AgendaForm(forms.ModelForm):
    year = forms.TypedChoiceField(
        coerce=int, choices=year_choices, initial=current_year)
    
    class Meta:
        model = Agenda
        fields = '__all__'


class IncomingMailForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'max': dt.now().date()}))
    
    class Meta:
        model = IncomingMail
        fields = '__all__'


class OutgoingMailForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'max': dt.now().date()}))
        
    class Meta:
        model = OutgoingMail
        fields = '__all__'


class IncomingDispositionForm(forms.ModelForm):
    class Meta:
        model = IncomingDisposition
        fields = '__all__'


class OutgoingDispositionForm(forms.ModelForm):
    class Meta:
        model = OutgoingDisposition
        fields = '__all__'
