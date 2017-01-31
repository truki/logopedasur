from django import forms

from .models import Paciente, Tutor, Sesion

class PacienteForm(forms.ModelForm):
    '''
    Formulario de tipo ModelForm para insertar un paciente
    '''

    class Meta:
        model = Paciente
        fields = '__all__'
