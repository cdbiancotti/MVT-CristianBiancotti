from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BusquedaGato

from .models import Gato


class ListadoGatos(ListView):
    model=Gato
    template_name = 'gato/listado_gatos.html'

    def get_queryset(self):
        apodo = self.request.GET.get('apodo', '')
        if apodo:
            object_list = self.model.objects.filter(apodo__icontains=apodo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaGato()
        return context
    
    
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