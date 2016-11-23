from django.db import models

# Create your models here.


class Paciente(models.Model):

    nombre = models.CharField(max_length=128, blank=False)
    apellidos = models.CharField(max_length=256, blank=True)
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=256, blank=True)
    imagen = models.ImageField(upload_to='pacientes', blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos
