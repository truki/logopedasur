from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Terapeuta
from .forms import TerapeutaForm


# Create your views here.

@login_required
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


# View for add new terapeutas

@login_required
def terapeutas_add(request):
    '''
    View that add a terapeuta into the system
    '''

    form = TerapeutaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('terapeutas:terapeutas_index'))

    context = {
        "form": form
    }
    return render(request, 'terapeutas_add.html', context)


@login_required
def terapeuta_detail(request, pk):
    '''
    View that show the terapeuta detail, terapeuta is retrieved by primary key
    '''
    terapeuta = get_object_or_404(Terapeuta, pk=pk)
    context = {"terapeuta": terapeuta}
    return render(request, 'terapeuta_detail.html', context)
