#panel de administracion.

from django.contrib import admin
from subject.models import Asignatura


# Register your models here.

admin.site.register(Asignatura)