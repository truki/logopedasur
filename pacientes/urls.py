from django.conf.urls import url
from pacientes import views

app_name = 'pacientes'
urlpatterns = [
    url(r'^$', views.index, name='pacientes_index'),
    url(r'^add/$', views.pacientes_add, name='pacientes_add'),
    url(r'^(?P<pk>\d+)/$', views.paciente_detail, name='paciente_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.paciente_edit, name='paciente_edit'),
    url(r'^sesion/(?P<pk>\d+)/$', views.sesion_detail, name='sesion_detail'),
    url(r'^sesion/add/$', views.sesion_add, name='sesion_add'),
    url(r'^tutor/add/$', views.tutor_add, name='tutor_add'),
    url(r'^tutor/$', views.tutores_list, name='tutores_list'),
    url(r'^tutor/(?P<pk>\d+)/edit/$', views.tutores_edit, name='tutores_edit'),
    url(r'^tutor/(?P<pk>\d+)/$', views.tutores_detail, name='tutores_detail'),
    url(r'^informe/add/$', views.informe_add, name='informe_add'),
    url(r'^(?P<pk>\d+)/horario/add/$', views.horario_paciente_add,
        name='horario_paciente_add'),
]
