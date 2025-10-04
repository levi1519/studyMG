from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.shortcuts import render
from django.urls import reverse_lazy
from hworks.forms import ActividadesForm
from django.utils import timezone
    
from datetime import datetime, time
from hworks.models import Actividades, Leccion, Examen
# Create your views here.




class ActividadesCreate(CreateView):
    model = Actividades
    form_class = ActividadesForm
    template_name = 'create_activity.html'
    success_url = reverse_lazy('hworks:activity_list')




class ActividadesList(ListView):
    model = Actividades
    template_name = 'activity_list.html'
    context_object_name = 'activity_list'

    
class ActividadesDetail(DetailView):
    model = Actividades
    template_name = 'activity_detail.html'
    context_object_name = 'activity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el objeto de actividad
        activity = self.get_object()
        
        # Agregar fecha límite y hora límite al contexto
        context['fecha_limite'] = activity.fecha_limite.strftime('%Y-%m-%d')
        context['hora_limite'] = activity.hora_limite.strftime('%H:%M')
        
        return context    




class ActividadesUpdate(UpdateView):
    model = Actividades
    template_name = 'activity_update.html'
    fields = [
        'tipo',
        'titulo',
        'asignatura',
        'notas',
        'recursos',
        'enlaces',
        'fecha_limite',
        'hora_limite',
        'prioridad',
        'calificacion',
        ]
    exclude = ['fecha_creacion','tiempo_restante']
    success_url = reverse_lazy('hworks:activity_list')

    def get_success_url(self):
        return reverse_lazy('hworks:activity_list')

class ActividadDelete(DeleteView):
    model = Actividades
    template_name = 'delete_activity.html'
    success_url = reverse_lazy('hworks:activity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activity'] = self.get_object()  # Agregar el objeto de la actividad al contexto
        return context
