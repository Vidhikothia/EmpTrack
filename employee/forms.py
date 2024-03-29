from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Employee

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', required=True)

    class Meta:
        model = Employee
        fields = {
            'username',
            'email',
            'password1',
            'password2',
            'department',
            'position',
        }


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter E-mail'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-Enter Password'
        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['department'].widget.attrs['placeholder'] = 'Enter Department'
        self.fields['position'].widget.attrs['class'] = 'form-control'
        self.fields['position'].widget.attrs['placeholder'] = 'Enter Position'
