from django.urls import path #Importamos Path
from appcoder.views import * #Importamos todas las vistas


#El archivo debe tener un archivo llamado exactamente urlpattern
urlpatterns = [
    path("inicio/",inicio, name="coder-inicio"),
    path("estudiantes/",estudiantes, name="coder-estudiantes"),
    path("profesores/",profesores, name="coder-profesores"),
    path("profesores/crear/",creacion_profesores, name="coder-profesores-crear"),
    path("cursos/",cursos, name="coder-cursos"),
    path("cursos/crear/",creacion_curso, name="coder-cursos-crear"),
    path("entregables/",entregables, name="coder-entregables"),
]