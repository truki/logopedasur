from django.db import models

from terapeutas.models import Terapeuta

# Create your models here.


class DiasAux (models.Model):
    '''
    Auxiliar Table to storage days a week and its properties
    '''

    DIAS_CHOICES = (
        ("L", "Lunes"),
        ("M", "Martes"),
        ("X", "Miércoles"),
        ("J", "Jueves"),
        ("V", "Viernes"),
        ("S", "Sábados"),
        ("D", "Domingos"),
    )
    dia = models.CharField(choices=DIAS_CHOICES, max_length=9)
    laborable = models.BooleanField()

    def __str__(self):
        return self.dia


class Horario (models.Model):
    '''
        Tabla Horario
        Donde se generaran todas y cada una de las sesiones
        individuales realizadas, tanto las periodicas como las que no tengan
        periodicidad
    '''

    terapeutas = models.ManyToManyField(Terapeuta)
    paciente = models.ForeignKey('pacientes.Paciente',
                                 on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_ini = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    hora_fin = models.TimeField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellidos + " " + self.fecha.strftime('%d/%m/%Y') + self.hora_ini.strftime('%H:%M') + "-" + self.hora_fin.strftime('%H:%M')


class ReglasHorario (models.Model):
    '''
        Tabla ReglasHorario
        Contiene todas las reglas periodicas de horarios de paciente
        que en algun momento en el tiempo seran volcadas en sesiones reales en
        la tabla horario
    '''

    terapeutas = models.ManyToManyField(Terapeuta)
    paciente = models.ForeignKey('pacientes.Paciente',
                                 on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    dias = models.ManyToManyField(DiasAux)
    hora_ini = models.TimeField(auto_now=False, auto_now_add=False, null=False)
    hora_fin = models.TimeField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellidos + " " + self.fecha.strftime('%d/%m/%Y') + self.hora_ini.strftime('%H:%M') + "-" + self.hora_fin.strftime('%H:%M')
