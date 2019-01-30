from django.db import models

# Create your models here.
# aquesta clase tipo MODEL és l'equivalent a una TAULA amb les seves respectives columnes dins una base de dades
class Project(models.Model):
    #charfield = cadena de caracteres
    title = models.CharField(max_length=200, verbose_name='Título')
    #textfield = campo de texto (més gran)
    description = models.TextField(verbose_name='Descripción')
    #imagefield = camp d'imatges
    #upload to = dins la carpeta media on es guarden els archius media, les imatges es guardaran a media/projects/
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    #datetime = camp de data i hora (auto_now_add=True, aquest cap s'auto emplenará amb l'hora real que se crei)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado día')
    #(auto_now_add=True, aquest cap s'auto emplenará amb l'hora real quan s'actualitza el camp)
    updated = models.DateTimeField(auto_now=True, verbose_name='Modificado día')

    #sub clase para configurar la clase con metadatos
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        #configuracion del orden en que deben estar los proyectos
        #en este caso ordenado por creación, de más reciente a más antiguo
        #por defecto lo organiza de mayor a menor (de más antiguo a nuevo)
        #por tanto si queremos que lo haga al revés ponemos signo negativo (-) delante
        ordering = ["-created"]
    
    #siempre nos devolvera el nombre que le hayamos especificado en title
    def __str__(self):
        return self.title