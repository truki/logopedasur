from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django import forms
from main.forms import UsuarioForm, PerfilTerapeutaForm

# Create your views here.


# Vista que renderiza el home de nuestro portal
# en caso de que el usuario no haya iniciado sesión se redirección a la
# al formulario de login
@login_required
def index(request):
    return render(request, 'index.html', {})


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
