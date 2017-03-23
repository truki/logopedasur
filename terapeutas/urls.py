from django.conf.urls import url
from terapeutas import views

app_name = 'terapeutas'
urlpatterns = [
    url(r'^$', views.index, name='terapeutas_index'),
    url(r'^(?P<pk>\d+)/$', views.terapeuta_detail, name='terapeuta_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.terapeuta_edit, name='terapeuta_edit'),
    url(r'^add/$', views.terapeutas_add, name='terapeutas_add'),
]
