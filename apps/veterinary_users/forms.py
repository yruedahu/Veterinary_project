from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    email = forms.EmailField(label="Correo electrónico", required=True)
    first_name = forms.CharField(label="Nombre(s)", max_length=150, required=True)
    last_name = forms.CharField(label="Apellidos", max_length=150, required=True)
    phone = forms.CharField(label="Teléfono", max_length=15, required=True)
    address = forms.CharField(label="Dirección", widget=forms.Textarea, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'first_name': 'Nombre(s)',
            'last_name': 'Apellidos',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }