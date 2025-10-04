from django.shortcuts import render
from django.views.generic import ListView , DetailView, CreateView, DeleteView, UpdateView
from schedule.models import Horario
from subject.models import Asignatura
from django.contrib import messages
from schedule.forms import HorarioForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.

class HorarioList(ListView):
    model = Horario
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'
    
    def get_queryset(self):
        # Ordenar los horarios primero por día de la semana y luego por hora de inicio
        return Horario.objects.all().order_by('dia_semana', 'hora_inicio')

    
       

class HorarioDetail(DetailView):
    model = Horario
    template_name = 'schedule_detail.html'
    context_object_name = 'schedule'



class HorarioCreate(CreateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'create_schedule.html'
    success_url = reverse_lazy('schedule:schedule_list')

    

   


class HorarioDelete(DeleteView):
    model = Horario
    template_name = 'delete_schedule.html'
    success_url =  reverse_lazy('schedule:schedule_list')



class HorarioUpdate(UpdateView):
    model = Horario
    template_name = 'update_schedule.html'
    fields = ['asignatura', 'dia_semana', 'hora_inicio', 'hora_fin']
    success_url = reverse_lazy('schedule:schedule_list')
