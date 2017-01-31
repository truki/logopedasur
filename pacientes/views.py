from django.shortcuts import render

from .models import Paciente, Tutor, Sesion

# Create your views here.


def index(request):
    '''
        Vista que muestra todos los pacientes
    '''
    pacientes = Paciente.objects.all()
    context = {"pacientes": pacientes}
    return render(request, "pacientes_index.html", context)


# View that show the patient detail, patient is retrieved by primary key
def paciente_detail(request, pk):
    pass


# View that show the sesion detail. Sesion is retrieved by its primary key (pk)
def sesion_detail(request, pk):
    pass
