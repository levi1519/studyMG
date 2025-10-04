from django.db import models


# Create your models here.
class Asignatura(models.Model):
    TIPO_ASIGNATURA_CHOICES = [
        ('Practica','Practica'),
        ('Teorica', 'Teorica'),
    ]

    MODALIDAD_CHOICES = [
        ('Virtual','Virtual'),
        ('Presencial','Presencial'),
    ]

    
    # Lógica que utiliza Horario

  

    titulo = models.CharField(max_length=100)
    profesor = models.CharField(max_length = 100)
    descripcion = models.TextField(blank = True)
    tipo_asignatura = models.CharField(max_length = 40, choices = TIPO_ASIGNATURA_CHOICES)
    modalidad = models.CharField(max_length = 20, choices = MODALIDAD_CHOICES)
    url_clases_grabadas = models.URLField(null = True, blank = True)

   
     

    def __str__(self):
        return self.titulo  # Simplemente retorna el título

    def get_horarios_display(self):
        horarios = self.horarios.all()
        if horarios:
            horario_str = ", ".join([f"{horario.dia_semana}:{horario.hora_inicio}--{horario.hora_fin}" for horario in horarios])
            return f"{self.titulo} - {horario_str}"
        else:
            return f"{self.titulo} - Horario no registrado"
    







