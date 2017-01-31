from django.contrib.auth.decorators import login_required
from django.shortcuts import render


from .models import Paciente, Tutor, Sesion
from .forms import PacienteForm

# Create your views here.

@login_required
def index(request):
    '''
        Vista que muestra todos los pacientes
    '''
    pacientes = Paciente.objects.all()
    context = {"pacientes": pacientes}
    return render(request, "pacientes_index.html", context)

# View that add a patient into the system
def pacientes_add(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('index'))

    context = {
        "form": form
    }
    return render(request, 'pacientes_add.html', context)

# View that show the patient detail, patient is retrieved by primary key
@login_required
def paciente_detail(request, pk):
    pass


# View that show the sesion detail. Sesion is retrieved by its primary key (pk)
@login_required
def sesion_detail(request, pk):
    pass
