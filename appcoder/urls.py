from django.urls import path #Importamos Path
from appcoder.views import * #Importamos todas las vistas


#El archivo debe tener un archivo llamado exactamente urlpattern
urlpatterns = [
    path("",inicio),
    path("estudiantes/",estudiantes),
    path("profesores/",profesores),
    path("cursos/",cursos),
    path("entregables/",entregables),
]