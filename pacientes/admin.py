from django.contrib import admin
from .models import Paciente, Sesion, Tutor, Informe, Evento, TipoEventoAux, EstadoPacienteAux

# Register your models here.


admin.site.register(Paciente)
admin.site.register(Sesion)
admin.site.register(Tutor)
admin.site.register(Informe)
admin.site.register(TipoEventoAux)
admin.site.register(Evento)
admin.site.register(EstadoPacienteAux)
