from django import forms
from hworks.models import Actividades
from subject.models  import Asignatura


class ActividadesForm(forms.ModelForm):
    class Meta:
        model = Actividades
        exclude = ['tiempo_restante']

    # Método constructor de la clase HorarioForm.
    def __init__(self, *args, **kwargs):
        # Llamada al método constructor de la clase base (ModelForm) para inicializar el formulario.
        super(ActividadesForm, self).__init__(*args, **kwargs)
        # Establece el queryset del campo 'asignatura' para incluir todas las instancias de Asignatura disponibles.
        self.fields['asignatura'].queryset = Asignatura.objects.all()
        # Personaliza la representación de cada instancia de Asignatura en el formulario.
        # Utiliza el título de la Asignatura como representación en lugar de la cadena devuelta por el método __str__.
        self.fields['asignatura'].label_from_instance = lambda obj: "%s" % obj.titulo