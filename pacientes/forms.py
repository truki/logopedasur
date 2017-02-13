from django import forms

from .models import Paciente, Tutor, Sesion

class PacienteForm(forms.ModelForm):
    '''
    Formulario de tipo ModelForm para insertar un paciente
    '''
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'tutor': forms.Select(attrs={'class': 'form-control'}),
        }


class TutorForm(forms.ModelForm):
    '''
    Formulario para insertar un nuevo tutor
    '''
    class Meta:
        model = Tutor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
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
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'format': '%m/%d/%Y'}),
            'hora_ini': forms.DateTimeInput(attrs={'class': 'form-control', 'format': '%H:%M'}),
            'hora_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'format': '%H:%M'}),
            'info': forms.Textarea(attrs={'class': 'form-control'}),
            'doc': forms.FileInput(attrs={'class': 'form-control'}),
        }
