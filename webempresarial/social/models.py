from django.db import models

# Create your models here.

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length= 100, unique= True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length= 200, null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta: # cuando se llame a esta clase cómo tipo de objeto, 
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ["name"] # el "-"  indica que es desde el más nuevo al más antiguo
    
    def __str__(self):
        return self.name