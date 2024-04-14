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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('agenda')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))


class IncomingMailForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'max': dt.now().date()}))

    class Meta:
        model = IncomingMail
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('incoming_mail')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Set the user for the instance
        if commit:
            instance.save()
        return instance


class OutgoingMailForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'max': dt.now().date()}))

    class Meta:
        model = OutgoingMail
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('outgoing_mail')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Set the user for the instance
        if commit:
            instance.save()
        return instance


class IncomingDispositionForm(forms.ModelForm):
    class Meta:
        model = IncomingDisposition
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('incoming_disposition')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Set the user for the instance
        if commit:
            instance.save()
        return instance


class OutgoingDispositionForm(forms.ModelForm):
    class Meta:
        model = OutgoingDisposition
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('outgoing_disposition')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.user = user
        # self.fields['mail'].queryset = OutgoingMail.objects.exclude(outgoingdisposition__isnull=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user  # Set the user for the instance
        if commit:
            instance.save()
        return instance
