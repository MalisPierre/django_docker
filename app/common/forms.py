from django import forms
from django.contrib.auth.models import User

class UserConnectionForm(forms.Form):
    pseudo = forms.CharField(label='Nom du compte')
    password = forms.CharField(widget=forms.PasswordInput())

class UserCreationForm(forms.Form):
    email = forms.CharField(label='email')
    pseudo = forms.CharField(label='Nom du compte')
    password = forms.CharField(widget=forms.PasswordInput())

class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

class ChangeEmailForm(forms.Form):
    email = forms.CharField(label='email')

class UserConnectionModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']