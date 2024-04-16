from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, HTML, Field, Layout
from django.urls import reverse_lazy
from django import forms


class UserLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('login')
        self.helper.form_method = 'POST'
        self.helper.layout = Div(
            Field('username', css_class='form-control'),
            Field('password', css_class='form-control'),
            Field('remember_me', css_class='form-check-input mt-3'),
            Div(
                HTML('<a href="{}" class="float-left mt-3">Forgot Password?</a>'.format(
                    reverse_lazy('reset_password'))),
                css_class="form-group"
            ),
            Div(
                Submit('submit', 'Login',
                       css_class="btn btn-primary btn-lg btn-icon icon-right"),
                css_class="text-right"
            ),
            css_class="form-group"
        )


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
