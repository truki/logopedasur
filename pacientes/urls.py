from django.conf.urls import url
from pacientes import views

app_name = 'pacientes'
urlpatterns = [
    url(r'^$', views.index, name='pacientes_index'),
    url(r'^add/$', views.pacientes_add, name='pacientes_add'),
    url(r'^(?P<pk>\d+)/$', views.paciente_detail, name='paciente_detail'),
    url(r'sesion/^(?P<pk>\d+)/$', views.sesion_detail, name='sesion_detail'),
    url(r'sesion/add/$', views.sesion_add, name='sesion_add'),
    url(r'^tutor/add/$', views.tutor_add, name='tutor_add'),
]
