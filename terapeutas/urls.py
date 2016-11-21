from django.conf.urls import url
from terapeutas import views

urlpatterns = [
    url(r'^$', views.index2, name='index'),
]
