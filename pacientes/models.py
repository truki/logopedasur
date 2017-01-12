from django.db import models
from django.core.urlresolvers import reverse

from terapeutas.models import Terapeuta

# Create your models here.


class Paciente(models.Model):
    '''
        Tabla Pacientes
    '''

    nombre = models.CharField(max_length=128, blank=False)
    apellidos = models.CharField(max_length=256, blank=True)
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=256, blank=True)
    imagen = models.ImageField(upload_to='pacientes', blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def get_absolute_url(self):
        url_name = paciente_detail
        return reverse(url_name, kwargs={"pk": self.id})


class Sesion(models.Model):
    '''
        Tabla sesiones
    '''

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    terapeutas = models.ManyToManyField(Terapeuta)
    fecha = models.DateField()
    hora_ini = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    hora_fin = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    info = models.TextField()
    doc = models.FileField(upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellidos + " "
        + self.fecha.strftime('%d/%m/%Y')
