from django.conf.urls import url
from terapeutas import views

app_name = 'terapeutas'
urlpatterns = [
    url(r'^$', views.index, name='terapeutas_index'),
]
