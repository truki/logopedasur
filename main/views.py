from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms
from main.forms import UsuarioForm, PerfilTerapeutaForm

from pacientes.models import Paciente, EstadoPacienteAux, TipoEventoAux


# Create your views here.


# Vista que renderiza el home de nuestro portal
# en caso de que el usuario no haya iniciado sesión se redirección a la
# al formulario de login
@login_required
def index(request):

    # Comprobamos tabla auxiliar EstadoPacienteAux
    estadosPacientes = EstadoPacienteAux.objects.count()
    if estadosPacientes > 0:
        estadosPacientesAux = True
    else:
        estadosPacientesAux = False

    tiposEvento = TipoEventoAux.objects.count()
    if tiposEvento > 0:
        tiposEventoAux = True
    else:
        tiposEventoAux = False


    total_pacientes = Paciente.objects.count()
    if total_pacientes > 0:
        enTerapia_pacientes = Paciente.objects.filter(estado__pk=2).count()
        enTerapia_pacientes_porciento = int((enTerapia_pacientes * 100) / total_pacientes)
        enAlta_pacientes = Paciente.objects.filter(estado__pk=3).count()
        enAlta_pacientes_porciento = int((enAlta_pacientes * 100) / total_pacientes)
        otros_pacientes = total_pacientes - enTerapia_pacientes - enAlta_pacientes
        otros_pacientes_porciento = int((otros_pacientes * 100) / total_pacientes)
    else:
        enTerapia_pacientes = 0
        enTerapia_pacientes_porciento = 0
        enAlta_pacientes = 0
        enAlta_pacientes_porciento = 0
        otros_pacientes = 0
        otros_pacientes_porciento = 0

    context = {"total_pacientes": total_pacientes,
               "enTerapia_pacientes": enTerapia_pacientes,
               "enTerapia_pacientes_porciento": enTerapia_pacientes_porciento,
               "enAlta_pacientes": enAlta_pacientes,
               "enAlta_pacientes_porciento": enAlta_pacientes_porciento,
               "otros_pacientes": otros_pacientes,
               "otros_pacientes_porciento": otros_pacientes_porciento,
               "estadosPacienteAux": estadosPacientesAux,
               "tiposEventoAux": tiposEventoAux }

    return render(request, 'index.html', context)


# Vista relacionada con el registro de un usuario
def registrarUsuario(request):

    registered = False

    if request.method == 'POST':
        usuario_form = UsuarioForm(data=request.POST)
        perfil_terapeuta_form = perfilTerapeutaForm(data=request.POST)

        if usuario_form.is_valid() and perfilTerapeutaForm.is_valid():
            user = usuario_form.save()
            user.set_password(user.password)
            user.save()

            perfil = PerfilTerapeutaForm.save(commit=False)
            perfil.user = user

            registered = True
        else:
            print(usuario_form.errors, perfil_terapeuta_form.errors)
    else:
        usuario_form = UsuarioForm()
        perfil_terapeuta_form = PerfilTerapeutaForm()

    return render(request, 'signup.html',
                  {'usuario_form': usuario_form,
                   'perfil_terapeuta_form': perfil_terapeuta_form,
                   'registered': registered})


# Vista para renderizar el formulario de login

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(username, password)
        # Si tenemos un objeto user los detalles son correcrtos
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("La cuenta está deshabilitada")
        else:
            print("Login inválido: {0}, {1}".format(username, password))
            return HttpResponse("Incio de sesión no válido.")
    else:
        return render(request, 'login.html', {})
