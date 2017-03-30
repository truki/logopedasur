from django.db import models
from django.core.urlresolvers import reverse

from terapeutas.models import Terapeuta

# Create your models here.

class Tutor(models.Model):
    '''
        Tabla de Tutores
    '''

    nombre = models.CharField(max_length=128, blank=False)
    apellidos = models.CharField(max_length=256, blank=True)
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=256, blank=True)
    cod_postal = models.DecimalField(max_digits=5, decimal_places=0,
                                     blank=True, null=True)
    localidad = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    imagen = models.ImageField(upload_to='tutores', null=True, blank=True)


    def __str__(self):
        return self.nombre + " " + self.apellidos

    def get_absolute_url(self):
        url_name = tutor_detail
        return reverse(url_name, kwargs={"pk": self.id})

class PacienteManager(models.Manager):
    def get_Leo(self):
        return super(PacienteManager, self).filter(nombre="Leo")


class EstadoPacienteAux(models.Model):
    '''
    Tabla auxililar para almacenar los estados de un paciente
    Entrevista preliminar, En Terapia, Alta, Pendiente de Valoracion medica,
    Pendiente de valoración educativa, Alta temporal, otro
    '''

    estado = models.CharField(max_length=128, blank=True, null=True)
    descripcion_estado = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.estado



class Paciente(models.Model):
    '''
        Tabla Pacientes
    '''

    nombre = models.CharField(max_length=128, blank=False)
    apellidos = models.CharField(max_length=256, blank=True)
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=256, blank=True)
    imagen = models.ImageField(upload_to='pacientes', null=True, blank=True)
    cod_postal = models.DecimalField(max_digits=5, decimal_places=0,
                                     blank=True, null=True)
    localidad = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=256, blank=True)
    estado = models.ForeignKey(EstadoPacienteAux, blank=True, null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, blank=True, null=True)
    terapeutas = models.ManyToManyField(Terapeuta)


    objects = models.Manager()  # Default model manager
    manager = PacienteManager()  # Paciente model manager

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
    doc = models.FileField(upload_to='pacientes/uploads/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.paciente.nombre + " " + self.paciente.apellidos + " "
        + self.fecha.strftime('%d/%m/%Y')

    def get_absolute_url(self):
        url_name = sesion_detail
        return reverse(url_name, kwargs={"pk": self.id})

class Informe(models.Model):
    '''
        Tabla informes
    '''

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    terapeutas = models.ManyToManyField(Terapeuta)
    titulo = models.CharField(max_length=256, blank=True, null=True)
    fecha_informe = models.DateField(blank=True, null=True)
    fecha_modificacion = models.DateField(auto_now_add=True)
    fichero = models.FileField(upload_to='pacientes/uploads/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.paciente.nombre + " "
        + self.fecha_informe.strftime('%d/%m/%Y') + self.titulo

class TipoEventoAux(models.Model):
    '''
    Clase auxialiar donde se almacenan los tipos de eventos:
    * Sesion.
    * Informe.
    * Familiar.
    * Escolar.
    * Medico
    * Otro
    '''

    nombre = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    '''
    Clase que almacenará un registro se todos los eventos de un paciente,
    sesiones, informes, y cualquier otro que merezca interes.
    Cuando en las tablas Sesion e Informe se inserte un registro, se
    inserta un evento del tipo correspondiente en esta tabla
    '''
    fecha = models.DateField()
    paciente = models.ForeignKey(Paciente)
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, null=True, blank=True)
    informe = models.ForeignKey(Informe, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=256, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey(TipoEventoAux)

    def __str__(self):
        return self.paciente.nombre + " " + self.fecha.strftime('%d/%m/%Y') + " " + self.tipo.nombre
