from django.conf.urls import url
from pacientes import views

app_name = 'pacientes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
