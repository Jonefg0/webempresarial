from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta: # cuando se llame a esta clase cómo tipo de objeto, 
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"] # el "-"  indica que es desde el más nuevo al más antiguo
    
    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image  = models.ImageField(verbose_name="Imagen", upload_to="blog/images/", null= True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    class Meta: # cuando se llame a esta clase cómo tipo de objeto, 
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"] # el "-"  indica que es desde el más nuevo al más antiguo
    
    def __str__(self):
        return self.title
    

