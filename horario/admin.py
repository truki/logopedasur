from django.contrib import admin
from .models import Horario, ReglasHorario, DiasAux

# Register your models here.

admin.site.register(Horario)
admin.site.register(ReglasHorario)
admin.site.register(DiasAux)
