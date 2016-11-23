from django import forms
from django.contrib.auth.models import User

from terapeutas.models import Terapeuta


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class PerfilTerapeutaForm(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = ('nombre', 'apellidos', 'dni')
