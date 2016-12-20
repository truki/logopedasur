from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    '''
        Vista para mostrar el listado de terapeutas
    '''
    return render(request, 'terapeutas_index.html', {})
