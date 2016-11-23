from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Terapeuta (models.Model):

    # OneToOne relation with User nmodel
    user = models.OneToOneField(User, null=True, blank=True)

    nombre = models.CharField(max_length=128, blank=False)
    apellidos = models.CharField(max_length=256, blank=False)
    dni = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=256, blank=False)
    cod_postal = models.DecimalField(max_digits=5, decimal_places=0)
    localidad = models.CharField(max_length=128, blank=True)
    provincia = models.CharField(max_length=128, blank=True)
    seg_social = models.CharField(max_length=12, blank=True, default="")
    imagen = models.ImageField(upload_to='terapeutas', blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellidos
