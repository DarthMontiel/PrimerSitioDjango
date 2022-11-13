from django.shortcuts import render
from appcoder.models import Curso,Estudiante,Profesor,Entregable
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html") #Esto es un loader a otro nivel y más corto

def cursos(request):
    return HttpResponse("Estas en Cursos")

def estudiantes(request):
    return HttpResponse("Estas en Estudiantes")

def profesores(request):
    return HttpResponse("Estas en Profesores")

def entregables(request):
    return HttpResponse("Estas en entregables")
