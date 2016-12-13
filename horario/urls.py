from django.conf.urls import url
from horario import views

app_name = 'horario'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
