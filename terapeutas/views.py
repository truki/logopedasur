from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import Terapeuta


# Create your views here.

def index(request):
    '''
        Vista para mostrar el listado de terapeutas
    '''
    terapeutas = Terapeuta.objects.all().order_by('apellidos','nombre')
    paginator = Paginator(terapeutas, 8) # show 8 therapeutas

    page = request.GET.get('page')
    try:
        terapeutas = paginator.page(page)
    except PageNotAnInteger:
        # si pagina no es un entero posicionamos en la primera
        terapeutas = paginator.page(1)
    except:
        # si la pagina está fuera de rango por arriba, nos
        # posicionamos en la última
        terapeutas = paginator.page(paginator.num_pages)

    return render(request, 'terapeutas_index.html', {"terapeutas": terapeutas})


# View for a new terapeutas

def new(request):
    pass
