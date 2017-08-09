from django import forms

from .models import Terapeuta
from pacientes.models import Sesion, Informe

class TerapeutaForm(forms.ModelForm):
    '''
    Formulario de tipo ModelForm para insertar un Terapeuta
    '''
    class Meta:
        model = Terapeuta
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'cod_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'seg_social': forms.TextInput(attrs={'class': 'form-control'}),
            'titulaciones': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class SesionForm(forms.ModelForm):
    '''
    Formulario para insertar un nuevo tutor
    '''
    class Meta:
        model = Sesion
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'terapeutas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_ini': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_fin': forms.TextInput(attrs={'class': 'form-control'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
            'doc': forms.FileInput(attrs={'class': 'form-control'}),
        }

class InformeForm(forms.ModelForm):
    '''
    Formulario para insertar un nuevo informe
    '''
    class Meta:
        model = Informe
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'terapeutas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'fecha_informe': forms.TextInput(attrs={'class': 'form-control'}),
            'fichero': forms.FileInput(attrs={'class': 'form-control'}),
        }
