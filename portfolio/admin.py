from django.contrib import admin
#importamos nuestro modelo Project (el punt davant models significa que està dins el mateix directori)
from .models import Project
# Register your models here.

#creamos una clase ProjectAdmin para la configuracion de los proyectos  
class ProjectAdmin(admin.ModelAdmin):
    #nos permite poder visualizar los campos que no són visibles incialmente (ya que no son modificables manualmente)
    #los crearemos en modo (SOLO LECTURA)
    readonly_fields = ('created', 'updated')

#registramos el proyecyo
#le pasamos como segundo parámetro la clase creada ProjectAdmin para tener una configuración extendida
admin.site.register(Project, ProjectAdmin)