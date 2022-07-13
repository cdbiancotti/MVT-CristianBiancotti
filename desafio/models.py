from django.db import models
from ckeditor.fields import RichTextField


class Perro(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    descripcion = RichTextField(null=True)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'Soy un perro llamado {self.nombre}'
