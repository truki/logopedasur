from django import forms

from .models import Terapeuta

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
