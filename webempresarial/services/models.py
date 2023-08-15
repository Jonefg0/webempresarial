from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image  = models.ImageField(verbose_name="Imagen", upload_to="services/images/")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta: # cuando se llame a esta clase cómo tipo de objeto, 
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
        ordering = ["-created"] # el "-"  indica que es desde el más nuevo al más antiguo
    
    def __str__(self):
        return self.title
    



