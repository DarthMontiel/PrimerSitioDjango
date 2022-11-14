from django.contrib import admin
from appcoder.models import * #Importamos los modelos al archivo

# Register your models here.
#Usamos la función admin.site.register para hacer el enlace

admin.site.register(Curso) #Enlazamos el modelo Curso
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)