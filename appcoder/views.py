from django.shortcuts import render
from appcoder.models import Curso,Estudiante,Profesor,Entregable
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "appcoder/index.html") #Esto es un loader a otro nivel y más corto

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")
