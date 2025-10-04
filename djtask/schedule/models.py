#Modelo de todos los horarios
from django.db import models


# Create your models here.

class Horario(models.Model):
    DIA_SEMANA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),

    ]
    
    
    asignatura = models.ForeignKey('subject.Asignatura', on_delete=models.CASCADE, related_name='horarios')  # 'subject.Asignatura' indica el modelo relacionado
    dia_semana = models.CharField(max_length=20, choices=DIA_SEMANA_CHOICES)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    
    

    def __str__(self):
        return f"{self.asignatura.titulo} - {self.dia_semana} - {self.hora_inicio} - {self.hora_fin}"
