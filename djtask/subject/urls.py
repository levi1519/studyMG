# Url para gestión de enlaces entre asignatiuras académicas
# Permite administrar enlaces del modulo asignaturas


"""
URL configuration for djtask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from schedule.views import ListaAsignaturas, CrearAsignatura, DetalleAsignatura, ActualizarAsignatura, EliminarAsignatura, Home


app_name = 'subject'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home.as_view(), name = 'home'),
    path('asignaturas/', ListaAsignaturas.as_view(), name = 'subject_list'),
    path('asignaturas/crear/', CrearAsignatura.as_view(), name= 'create_subject'),
    path('asignaturas/<int:pk>/', DetalleAsignatura.as_view(), name='detail_subject'),
    path('asignaturas/<int:pk>/actualizar/', ActualizarAsignatura.as_view(), name='update_subject'),
    path('asignaturas/<int:pk>/eliminar/', EliminarAsignatura.as_view(), name= 'delete_subject'),
 

]
    


    
