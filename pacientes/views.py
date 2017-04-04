from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


from .models import Paciente, Tutor, Sesion, Informe, Evento, TipoEventoAux
from .forms import PacienteForm, TutorForm, SesionForm, InformeForm, EventoForm
from horario.forms import HorarioForm
from horario.models import ReglasHorario

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
    print("request.POST {0}".format(request.POST))
    if form.is_valid():
        print("HE PASADO POR is_valid() !!!!!!!!!!!!!!!!!")
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, "Se ha insertado un Paciente")
        return HttpResponseRedirect(reverse('pacientes:pacientes_index'))

    context = {
        "form": form
    }
    print("NOOOOOOOO HE PASADO POR is_valid() !!!!!!!!!!!!!!!!!")
    return render(request, 'pacientes_add.html', context)


@login_required
def paciente_detail(request, pk):
    '''
    View that show the patient detail, patient is retrieved by primary key
    '''
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = Sesion.objects.filter(paciente=pk)
    informes = Informe.objects.filter(paciente=pk)
    horarios = ReglasHorario.objects.filter(paciente=pk)
    # excluded Sesion and Reports events in otroEventos query
    otroEventos = Evento.objects.filter(paciente=pk).exclude(tipo_id=1).exclude(tipo_id=2)

    formSesion = SesionForm(request.POST or None, request.FILES or None)
    formSesion.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formInforme = InformeForm(request.POST or None, request.FILES or None)
    formInforme.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formHorario = HorarioForm(request.POST or None)
    formHorario.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formEvento = EventoForm(request.POST or None)
    formEvento.fields["tipo"].queryset = TipoEventoAux.objects.all().exclude(pk=1).exclude(pk=2)
    formEvento.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    context = {"paciente": paciente, "formSesion": formSesion,
               "formInforme": formInforme, "formHorario": formHorario,
               "formEvento": formEvento, "sesiones_box": "visible",
               "informes_box": "hidden", "horario_box": "hidden",
               "eventos_box": "hidden", "sesiones": sesiones,
               "horarios": horarios, "informes": informes,
               "eventos": otroEventos}
    return render(request, 'paciente_detail.html', context)

@login_required
def paciente_edit(request, pk):
    '''
    View that show the patient edit form foor patient basic info,
    patient is retrieved by primary key
    '''
    paciente = get_object_or_404(Paciente, pk=pk)

    form = PacienteForm(request.POST or None, request.FILES or None,
                        instance=paciente)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, "Se ha editado el paciente " +
                         instance.nombre + " " +
                         instance.apellidos)
        return HttpResponseRedirect(reverse('pacientes:pacientes_index'))

    context = {
        "form": form,
        "paciente": paciente
    }
    return render(request, 'pacientes_edit.html', context)


# View that show the sesion detail. Sesion is retrieved by its primary key (pk)
@login_required
def sesion_detail(request, pk):
    pass


@login_required
def sesion_paciente_add(request, pk):
    '''
    View that add a tutor into the system
    '''
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = Sesion.objects.filter(paciente=pk)
    informes = Informe.objects.filter(paciente=pk)
    horarios = ReglasHorario.objects.filter(paciente=pk)
    # excluded Sesion and Reports events in otroEventos query
    otroEventos = Evento.objects.filter(paciente=pk).exclude(tipo_id=1).exclude(tipo_id=2)

    formSesion = SesionForm(request.POST or None, request.FILES or None)
    formSesion.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formInforme = InformeForm(request.POST or None, request.FILES or None)
    formInforme.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formHorario = HorarioForm(request.POST or None)
    formHorario.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formEvento = EventoForm(request.POST or None)
    formEvento.fields["tipo"].queryset = TipoEventoAux.objects.all().exclude(pk=1).exclude(pk=2)
    formEvento.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    context = {"paciente": paciente, "formSesion": formSesion,
               "formInforme": formInforme, "formHorario": formHorario,
               "formEvento": formEvento, "sesiones_box": "visible",
               "informes_box": "hidden", "horario_box": "hidden",
               "eventos_box": "hidden", "sesiones": sesiones,
               "horarios": horarios, "informes": informes,
               "eventos": otroEventos}

    if request.method == 'POST':
        form = SesionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return render(request, 'paciente_detail.html', context)


    return render(request, 'paciente_detail.html', context)


@login_required
def informe_paciente_add(request,pk):
    '''
    View that add a report to a patient
    '''
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = Sesion.objects.filter(paciente=pk)
    informes = Informe.objects.filter(paciente=pk)
    horarios = ReglasHorario.objects.filter(paciente=pk)
    # excluded Sesion and Reports events in otroEventos query
    otroEventos = Evento.objects.filter(paciente=pk).exclude(tipo_id=1).exclude(tipo_id=2)

    formSesion = SesionForm(request.POST or None, request.FILES or None)
    formSesion.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formInforme = InformeForm(request.POST or None, request.FILES or None)
    formInforme.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formHorario = HorarioForm(request.POST or None)
    formHorario.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formEvento = EventoForm(request.POST or None)
    formEvento.fields["tipo"].queryset = TipoEventoAux.objects.all().exclude(pk=1).exclude(pk=2)
    formEvento.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    context = {"paciente": paciente, "formSesion": formSesion,
               "formInforme": formInforme, "formHorario": formHorario,
               "formEvento": formEvento, "sesiones_box": "hidden",
               "informes_box": "visible", "horario_box": "hidden",
               "eventos_box": "hidden", "sesiones": sesiones,
               "horarios": horarios, "informes": informes,
               "eventos": otroEventos}

    if request.method == 'POST':
        form = InformeForm(request.POST or None, request.FILES or None)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return render(request, 'paciente_detail.html', context)

    return render(request, 'paciente_detail.html', context)


@login_required
def horario_paciente_add(request, pk):
    '''
    View that add a tutor into the system
    '''
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = Sesion.objects.filter(paciente=pk)
    informes = Informe.objects.filter(paciente=pk)
    horarios = ReglasHorario.objects.filter(paciente=pk)
    # excluded Sesion and Reports events in otroEventos query
    otroEventos = Evento.objects.filter(paciente=pk).exclude(tipo_id=1).exclude(tipo_id=2)

    formSesion = SesionForm(request.POST or None, request.FILES or None)
    formSesion.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formInforme = InformeForm(request.POST or None, request.FILES or None)
    formInforme.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formHorario = HorarioForm(request.POST or None)
    formHorario.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formEvento = EventoForm(request.POST or None)
    formEvento.fields["tipo"].queryset = TipoEventoAux.objects.all().exclude(pk=1).exclude(pk=2)
    formEvento.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    context = {"paciente": paciente, "formSesion": formSesion,
               "formInforme": formInforme, "formHorario": formHorario,
               "formEvento": formEvento, "sesiones_box": "hidden",
               "informes_box": "hidden", "horario_box": "visible",
               "eventos_box": "hidden", "sesiones": sesiones,
               "horarios": horarios, "informes": informes,
               "eventos": otroEventos}

    if request.method == 'POST':
        form = HorarioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return render(request, 'paciente_detail.html', context)

    return render(request, 'paciente_detail.html', context)

@login_required
def evento_paciente_add(request, pk):
    '''
    View that add an evento to a patient (pk)
    '''
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = Sesion.objects.filter(paciente=pk)
    informes = Informe.objects.filter(paciente=pk)
    horarios = ReglasHorario.objects.filter(paciente=pk)
    # excluded Sesion and Reports events in otroEventos query
    otroEventos = Evento.objects.filter(paciente=pk).exclude(tipo_id=1).exclude(tipo_id=2)

    formSesion = SesionForm(request.POST or None, request.FILES or None)
    formSesion.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formInforme = InformeForm(request.POST or None, request.FILES or None)
    formInforme.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formHorario = HorarioForm(request.POST or None)
    formHorario.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    formEvento = EventoForm(request.POST or None)
    formEvento.fields["tipo"].queryset = TipoEventoAux.objects.all().exclude(pk=1).exclude(pk=2)
    formEvento.fields["paciente"].queryset = Paciente.objects.filter(pk=pk)

    context = {"paciente": paciente, "formSesion": formSesion,
               "formInforme": formInforme, "formHorario": formHorario,
               "formEvento": formEvento, "sesiones_box": "hidden",
               "informes_box": "hidden", "horario_box": "hidden",
               "eventos_box": "visible", "sesiones": sesiones,
               "horarios": horarios, "informes": informes,
               "eventos": otroEventos}

    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request, 'paciente_detail.html', context)

    return render(request, 'paciente_detail.html', context)


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
def tutores_list(request):
    '''
    View that show the tutors of the patients
    '''

    tutores = Tutor.objects.all().order_by('apellidos', 'nombre')
    paginator = Paginator(tutores, 8)  # show 8 therapeutas

    page = request.GET.get('page')
    try:
        tutores = paginator.page(page)
    except PageNotAnInteger:
        # si pagina no es un entero posicionamos en la primera
        tutores = paginator.page(1)
    except:
        # si la pagina está fuera de rango por arriba, nos
        # posicionamos en la última
        tutores = paginator.page(paginator.num_pages)
    context = {"tutores": tutores}
    return render(request, "tutores_list.html", context)



@login_required
def tutores_detail(request, pk):
    '''
    View that show the tutors detail
    '''
    pass


@login_required
def tutores_edit(request, pk):
    '''
    View that show a form to edit the tutors detail
    '''
    tutor = get_object_or_404(Tutor, pk=pk)

    form = TutorForm(request.POST or None, request.FILES or None,
                        instance=tutor)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, "Se ha editado el tutor " +
                         instance.nombre + " " +
                         instance.apellidos)
        return HttpResponseRedirect(reverse('pacientes:tutores_list'))

    context = {
        "form": form,
        "tutor": tutor
    }
    return render(request, 'tutores_edit.html', context)
