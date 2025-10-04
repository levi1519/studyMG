from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView, DetailView,UpdateView,DeleteView, TemplateView
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy, reverse
from subject.models import  Asignatura
from schedule.models import Horario

# Create your views here.

class ListaAsignaturas(ListView):
    model = Asignatura
    template_name = 'subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        asignaturas = super().get_queryset()
        for asignatura in asignaturas:
            horarios = asignatura.horarios.all()
            # Crear una lista de cadenas de horario o una lista vacía si no hay horarios
            horarios_list = [f"{horario.dia_semana} {horario.hora_inicio}-{horario.hora_fin}" for horario in horarios] if horarios else []
            # Asigna la lista de cadenas de horario al atributo 'horarios_list' de la asignatura
            asignatura.horarios_list = horarios_list
        return asignaturas
    

class CrearAsignatura(CreateView):
    model = Asignatura
    fields = ['titulo', 'profesor', 'descripcion', 'tipo_asignatura', 'modalidad', 'url_clases_grabadas']
    template_name = 'create_subject.html'
    success_url = reverse_lazy('subject_list')

class DetalleAsignatura(DetailView):
    model = Asignatura
    template_name = 'detail_subject.html'
    context_object_name = 'subject'

class ActualizarAsignatura(UpdateView):
    model = Asignatura
    template_name = 'update_subject.html'
    fields = ['titulo','profesor','descripcion','tipo_asignatura','modalidad','url_clases_grabadas']
    success_url = reverse_lazy('subject_list')

class EliminarAsignatura(DeleteView):
    model = Asignatura
    template_name = 'delete_subject.html'
    success_url = reverse_lazy('subject_list')



class Home(TemplateView):
    template_name = 'home.html'