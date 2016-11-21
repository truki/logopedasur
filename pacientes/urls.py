from django.conf.urls import url
from pacientes import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
