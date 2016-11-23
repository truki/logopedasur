from django.shortcuts import render
from django import forms
from main.forms import UsuarioForm, PerfilTerapeutaForm

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


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
