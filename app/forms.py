from django import forms
from django.urls import reverse_lazy
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Div, HTML, Field, Layout
from .models import Agenda, IncomingMail, OutgoingMail, IncomingDisposition, OutgoingDisposition
import datetime
from datetime import datetime as dt

# Utils Function


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Forms Classes


class AgendaForm(forms.ModelForm):
    year = forms.TypedChoiceField(
        coerce=int, choices=[], initial=current_year, empty_value=None)

    class Meta:
        model = Agenda
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('agenda')
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

        existing_years = Agenda.objects.values_list('year', flat=True)
        year_choices = [("", "Select Year")]
        year_choices += [(year, year) for year in range(
            1984, current_year() + 1) if year not in existing_years]
        self.fields['year'].choices = year_choices


class BaseMailForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'min': '1984-01-01', 'max': dt.now().date()}))
    file = forms.FileField(help_text='Upload PDF file of mail', required=False)
    # agenda = forms.ModelChoiceField(queryset=Agenda.objects.all().order_by(
    #     'year'), empty_label='Select Agenda Year', help_text='Agenda year must match with Date')

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        # Automatically set the agenda field to the year of the date field
        instance.agenda = Agenda.objects.get_or_create(
            year=self.cleaned_data['date'].year)[0]
        if commit:
            instance.save()
        return instance

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date = cleaned_data.get('date')
    #     agenda = cleaned_data.get('agenda')
    #     if date.year != agenda.year:
    #         raise ValidationError("Date year must match the agenda year.")
    #     return cleaned_data


class IncomingMailForm(BaseMailForm):
    class Meta:
        model = IncomingMail
        fields = '__all__'
        exclude = ('user', 'agenda')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.helper.form_action = reverse_lazy('incoming_mail')


class OutgoingMailForm(BaseMailForm):
    class Meta:
        model = OutgoingMail
        fields = '__all__'
        exclude = ('user', 'agenda')

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.helper.form_action = reverse_lazy('outgoing_mail')


class BaseDispositionForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit'))

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class IncomingDispositionCreateForm(BaseDispositionForm):
    mail = forms.ModelChoiceField(queryset=IncomingMail.objects.exclude(
        incomingdisposition__isnull=False), empty_label='Select Incoming Mail')

    class Meta:
        model = IncomingDisposition
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.helper.form_action = reverse_lazy('incoming_disposition')


class IncomingDispositionUpdateForm(BaseDispositionForm):
    class Meta:
        model = IncomingDisposition
        fields = '__all__'
        exclude = ('user', 'mail')

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.helper.form_action = reverse_lazy(
            'incoming_disposition_update', kwargs={'pk': self.instance.id})


class OutgoingDispositionCreateForm(BaseDispositionForm):
    mail = forms.ModelChoiceField(queryset=OutgoingMail.objects.exclude(
        outgoingdisposition__isnull=False), empty_label='Select Outgoing Mail')

    class Meta:
        model = OutgoingDisposition
        fields = '__all__'
        exclude = ('user',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.helper.form_action = reverse_lazy('outgoing_disposition')


class OutgoingDispositionUpdateForm(BaseDispositionForm):
    class Meta:
        model = OutgoingDisposition
        fields = '__all__'
        exclude = ('user', 'mail')

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.helper.form_action = reverse_lazy(
            'outgoing_disposition_update', kwargs={'pk': self.instance.id})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('user_profile_update')
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Div(
                Div(
                    Field('username', css_class='form-control'),
                    css_class='col-md-5 col-12'
                ),
                Div(
                    Field('email', css_class='form-control'),
                    css_class='col-md-7 col-12'
                ),
                css_class='row'
            ),
            Div(
                HTML('<a href="{}" class="float-left mt-3">Change Password</a>'.format(
                    reverse_lazy('password_change'))),
                css_class="form-group col-12"
            ),
            Div(
                Submit('submit', 'Change Profile',
                       css_class="btn btn-primary btn-lg btn-icon icon-right"),
                css_class="text-right"
            )
        )
