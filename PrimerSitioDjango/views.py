from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludos(request):
    return HttpResponse("<center><h1>Hola Gente</h1></center>")

def diaHoy(request, nombre):
    hoy = datetime.now()
    respuesta = f"Hoy es: {hoy} - Bienvenid@ {nombre}"
    return HttpResponse(respuesta)

def vista_plantilla(request):
    #Diccionario con datos para la plantilla
    datos = {"nombre":"Eliseo", "fecha":datetime.now(),"Apellido":"Chavez"}
    
    #Usamos un Loader para cargar la plantilla en lugar del metodo anterior
    plantilla = loader.get_template("plantilla01.html")

    #Generamos el documento que recibira el HttpResponse
    documento = plantilla.render(datos)
    #Documento es un objeto tipo template y render debe recibir un objeto tipo context

    #Retornamos el HttpResponse con el documento
    return HttpResponse(documento)

def listado_alumnos(request):
     #Lista de alumnos
    lista_alumnos = ["Eliseo Chavez", "Sabine Kleiner", 
    "Pachelia Chavez", "Yismo Castrejon"]
    #Datos que vamos a pasarle al contexto
    datos = {"tecnologia":"Python", "listado_alumnos":lista_alumnos}


    #Cargamos la plantilla con loader.get_template("nombreDeLaPlantilla.html")
    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)

