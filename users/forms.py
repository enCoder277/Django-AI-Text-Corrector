from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input'}), label='Логин')     #не определен класс form-input в стилях

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),label='Пароль')  #не определен класс form-input в стилях
