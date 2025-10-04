from django.db import models
from subject.models import Asignatura

# Create your models here.

class Actividades(models.Model):
    TIPO_CHOICES = [
        ('Tarea','Tarea'),
        ('Taller','Taller'),        
        ('Exposicion','Exposicion'),
        ('TrabajoExperimental','Trabajo Experimental'),        
    ]
    
    PRIORIDAD_CHOICES = [
        ('Baja','Baja'),
        ('Media','Media'),
        ('Alta','Alta'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    titulo = models.CharField(max_length=100)   
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name='actividades_subject')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    recursos = models.FileField(upload_to='recursos/', blank=True, null=True)
    enlaces = models.URLField(blank=True)
    fecha_limite = models.DateField()
    hora_limite = models.TimeField(blank=False, null=False)
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_CHOICES)
    calificacion = models.FloatField(null=True, blank=True)
    tiempo_restante = models.DurationField(blank=True, null=True, editable=False)  # Nuevo campo para el tiempo restante

    def __str__ (self):
        return self.titulo


class Leccion(models.Model):

    PRIORIDAD_CHOICES = [
        ('Baja','Baja'),
        ('Media','Media'),
        ('Alta','Alta'),
    ]

    fecha_creacion = models.DateTimeField(auto_now_add = True)
    asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE,related_name='leccion_subject')
    titulo = models.CharField(max_length = 100)
    notas = models.TextField(blank = True)
    fecha_limite = models.DateTimeField()
    tiempo_restante = models.DurationField(blank=True, null=True)  # Nuevo campo para el tiempo restante
    enlaces = models.URLField(blank = True)
    recursos = models.FileField(upload_to='recursos/', blank=True, null=True)
    prioridad = models.CharField(max_length = 20, choices = PRIORIDAD_CHOICES)
    calificacion = models.FloatField(null = True, blank = True) 

    def __str__(self):
        return self.titulo
    

class Examen(models.Model):

    PRIORIDAD_CHOICES = [
        ('Baja','Baja'),
        ('Media','Media'),
        ('Alta','Alta'),
    ]
    
    asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE,related_name = 'examen_subject')   
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_limite = models.DateTimeField()
    titulo = models.CharField(max_length = 100)
    notas = models.TextField(blank = True)
    recursos = models.FileField()
    enlaces = models.URLField(blank = True)
    prioridad = models.CharField(max_length = 20, choices = PRIORIDAD_CHOICES)
    calificacion = models.FloatField(null = True, blank = True) 

    def __str__(self):
        return self.titulo