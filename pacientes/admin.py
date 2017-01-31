from django.contrib import admin
from .models import Paciente, Sesion, Tutor

# Register your models here.


admin.site.register(Paciente)
admin.site.register(Sesion)
admin.site.register(Tutor)
