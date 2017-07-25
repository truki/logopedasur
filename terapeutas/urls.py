from django.conf.urls import url
from terapeutas import views

app_name = 'terapeutas'
urlpatterns = [
    url(r'^$', views.index, name='terapeutas_index'),
    url(r'^(?P<pk>\d+)/$', views.terapeuta_detail, name='terapeuta_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.terapeuta_edit, name='terapeuta_edit'),
    url(r'^(?P<pk>\d+)/pacientes/$', views.pacientes_terapeuta, name='pacientes_terapeuta'),
    url(r'^(?P<pk>\d+)/sesiones/$', views.sesiones_terapeuta, name='sesiones_terapeuta'),
    url(r'^(?P<pk>\d+)/informes/$', views.informes_terapeuta, name='informes_terapeuta'),
    url(r'^add/$', views.terapeutas_add, name='terapeutas_add'),
    url(r'^(?P<pk>\d+)/sesion/add', views.sesion_terapeuta_add, name='sesion_trapeuta_add'),
    url(r'^(?P<pk>\d+)/evento/add', views.evento_terapeuta_add, name='evento_trapeuta_add'),
    url(r'^(?P<pk>\d+)/horario/add', views.horario_terapeuta_add, name='horario_trapeuta_add'),


]
