from django import forms

from .models import ReglasHorario, Horario, DiasAux

class HorarioForm(forms.ModelForm):
    '''
    Formulario para insertar un nuevo horario (regla)
    '''
    class Meta:
        model = ReglasHorario
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'terapeutas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'dia': forms.Select(attrs={'class': 'form-control'}),
            'hora_ini': forms.TextInput(attrs={'class': 'form-control'}),
            'hora_fin': forms.TextInput(attrs={'class': 'form-control'}),
        }
