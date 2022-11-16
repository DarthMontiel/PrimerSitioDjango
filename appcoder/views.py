from django.shortcuts import render
from appcoder.models import Curso,Estudiante,Profesor,Entregable
from appcoder.forms import ProfesorFormulario #Importamos el formulario de forms.py
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    cursos = Curso.objets.all()

    
    return render(request, "appcoder/index.html") #Esto es un loader a otro nivel y más corto

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")

def creacion_curso(request):
    if request.method == "POST":#Si el metodo es tipo recibido es tipo POST
        nombre_curso = request.POST["curso"] #Curso y camada se obtiene del nombre del formulario (campo "name")
        numero_camada = request.POST["camada"]

        curso = Curso(nombre=nombre_curso, camada=numero_camada) #Instanciamos el modelo curso donde se almacena la info del post
        curso.save()

    return render(request, "appcoder/curso_formulario.html")#Que debe renderizar la plantilla del formulario

def creacion_profesores(request):
    if request.method == "POST":
        #Creamos un formulario
        formulario = ProfesorFormulario(request.POST) #Podemos pasar el diccionario completo del request
        #sin crear uno como en creacion_curso

        #Validación que el formulario no tenga problemas
        if formulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()
            #Renderizamos una página nuevamente. Todas las vistas deben retornar una ista
            return render (request, "appcoder/index.html/"
            )
    else:
        formulario = ProfesorFormulario()

    contexto = {'formulario':formulario}
    return render (request, "appcoder/profesores_formularios.html",contexto)#Como tercer argumento pasamos un diccionario (que es el contexto)