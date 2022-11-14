from django.urls import path #Importamos Path
from appcoder.views import * #Importamos todas las vistas


#El archivo debe tener un archivo llamado exactamente urlpattern
urlpatterns = [
    path("inicio/",inicio, name="coder-inicio"),
    path("estudiantes/",estudiantes, name="coder-estudiantes"),
    path("profesores/",profesores, name="coder-profesores"),
    path("cursos/",cursos, name="coder-cursos"),
    path("entregables/",entregables, name="coder-entregables"),
]