from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gato


class ListadoGatos(ListView):
    model=Gato
    template_name = 'gato/listado_gatos.html'
    
class CrearGato(CreateView):
    model=Gato
    template_name = 'gato/crear_gato.html'
    success_url = '/mascotas/gatos'
    fields = ['apodo', 'edad', 'fecha_creacion']


class EditarGato(LoginRequiredMixin, UpdateView):
    model=Gato
    template_name = 'gato/editar_gato.html'
    success_url = '/mascotas/gatos'
    fields = ['apodo', 'edad', 'fecha_creacion']


class EliminarGato(LoginRequiredMixin, DeleteView):
    model=Gato
    template_name = 'gato/eliminar_gato.html'
    success_url = '/mascotas/gatos'


class MostrarGato(DetailView):
    model = Gato
    template_name = 'gato/mostrar_gato.html'