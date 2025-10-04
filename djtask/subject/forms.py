from django import forms
from subject.models import Asignatura

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['titulo','profesor','descripcion', 'tipo_asignatura','modalidad','url_clases_grabadas']
        