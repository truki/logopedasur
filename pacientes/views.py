from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from .models import Paciente, Tutor, Sesion
from .forms import PacienteForm, TutorForm, SesionForm

# Create your views here.


@login_required
def index(request):
    '''
        Vista que muestra todos los pacientes
    '''
    pacientes = Paciente.objects.all().order_by('apellidos', 'nombre')
    paginator = Paginator(pacientes, 8)  # show 8 therapeutas

    page = request.GET.get('page')
    try:
        pacientes = paginator.page(page)
    except PageNotAnInteger:
        # si pagina no es un entero posicionamos en la primera
        pacientes = paginator.page(1)
    except:
        # si la pagina está fuera de rango por arriba, nos
        # posicionamos en la última
        pacientes = paginator.page(paginator.num_pages)
    context = {"pacientes": pacientes}
    return render(request, "pacientes_index.html", context)


@login_required
def pacientes_add(request):
    '''
    View that add a patient into the system
    '''
    form = PacienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('pacientes:pacientes_index'))

    context = {
        "form": form
    }
    return render(request, 'pacientes_add.html', context)


@login_required
def paciente_detail(request, pk):
    '''
    View that show the patient detail, patient is retrieved by primary key
    '''
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = Sesion.objects.filter(paciente=pk)
    print(sesiones)
    formSesion = SesionForm(request.POST or None, request.FILES or None)
    context = {"paciente": paciente, "formSesion": formSesion,
               "sesiones_box": "visible", "informes_box": "hidden",
               "horario_box": "hidden", "sesiones": sesiones}
    return render(request, 'paciente_detail.html', context)



# View that show the sesion detail. Sesion is retrieved by its primary key (pk)
@login_required
def sesion_detail(request, pk):
    pass


@login_required
def tutor_add(request):
    '''
    View that add a tutor into the system
    '''
    form = TutorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('pacientes:pacientes_index'))

    context = {
        "form": form
    }
    return render(request, 'tutor_add.html', context)


@login_required
def sesion_add(request):
    '''
    View that add a tutor into the system
    '''
    if request.method == 'POST':
        form = SesionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('pacientes:pacientes_index'))

    print("Ok formulario NO valido")
    return render(request, 'pacientes_index.html', {})
