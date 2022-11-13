from django.shortcuts import render
from appcoder.models import Curso,Estudiante,Profesor,Entregable
from django.http import HttpResponse

# Create your views here.
def vista_curso (request):
    cursos = Curso.objects.all #Accedemos a todo lo que hay dentro del modelo Curso (en este caso los cursos en la DB) y lo guardamos en una "lista"
    cadena_respuesta = "" #Una cadena vacia solo para no crear de momento una plantilla

    for curso in cursos:
        cadena_respuesta += curso.nombre + " | " #Repasamos toda la lista generada arriba
    
    return HttpResponse(cadena_respuesta)
