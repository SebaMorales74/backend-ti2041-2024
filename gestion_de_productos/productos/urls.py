from django.urls import path

from . import views

urlpatterns = [
    path("consulta/", views.consulta, name="consulta"),
    path("registro/", views.registro, name="registro"),
    path("resultado/", views.resultado, name="resultado"),
]