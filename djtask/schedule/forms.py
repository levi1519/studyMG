from django import forms
from django.core.exceptions import ValidationError
from schedule.models import Horario
from subject.models import Asignatura

# Definición del formulario HorarioForm basado en el modelo Horario.
class HorarioForm(forms.ModelForm):
    # Meta clase que proporciona metadatos al formulario HorarioForm.
    class Meta:
        model = Horario  # Indica que el formulario se basa en el modelo Horario.
        fields = ['asignatura', 'dia_semana', 'hora_inicio', 'hora_fin']  # Campos del modelo que se incluirán en el formulario.
        # Widgets personalizados para algunos de los campos del formulario.
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type':'time'}),  # Se utiliza un widget de entrada de hora para hora_inicio.
            'hora_fin': forms.TimeInput(attrs={'type':'time'})  # Se utiliza un widget de entrada de hora para hora_fin.
        }

    # Método constructor de la clase HorarioForm.
    def __init__(self, *args, **kwargs):
        # Llamada al método constructor de la clase base (ModelForm) para inicializar el formulario.
        super(HorarioForm, self).__init__(*args, **kwargs)
        # Establece el queryset del campo 'asignatura' para incluir todas las instancias de Asignatura disponibles.
        self.fields['asignatura'].queryset = Asignatura.objects.all()
        # Personaliza la representación de cada instancia de Asignatura en el formulario.
        # Utiliza el título de la Asignatura como representación en lugar de la cadena devuelta por el método __str__.
        self.fields['asignatura'].label_from_instance = lambda obj: "%s" % obj.titulo

    # Método para la limpieza y validación de datos del formulario.
    def clean(self):
        # Llamada al método clean de la clase base para obtener los datos limpios.
        cleaned_data = super().clean()
        # Recupera la asignatura, día de la semana, hora de inicio y fin del formulario.
        dia_semana = cleaned_data.get('dia_semana')
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')

        # Verifica que la hora de inicio sea anterior a la hora de fin.
        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                # Añade el mensaje de error solo al campo hora_inicio.
                self.add_error('hora_inicio', "La hora de inicio debe ser anterior que la hora de fin")
            else:
                # Verifica que no haya solapamiento con otros horarios existentes.
                horarios_existentes = Horario.objects.filter(dia_semana=dia_semana)
                # Excluye el horario actual si estamos editando.
                if self.instance and self.instance.pk:
                    horarios_existentes = horarios_existentes.exclude(pk=self.instance.pk)

                for horario in horarios_existentes:
                    if (hora_inicio < horario.hora_fin and hora_fin > horario.hora_inicio):
                        # Añade el mensaje de error solo al campo hora_inicio.
                        self.add_error('hora_inicio', "Existe un horario existente dentro de este rango de horas, escoja otro por favor")
                        break

        # Retorna los datos limpios del formulario.
        return cleaned_data