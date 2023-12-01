from msilib.schema import Directory
from django.db import models
from datetime import date


class RepSolic(models.Model):
    Nombre = models.CharField('nombre',max_length=120) 
    Numero = models.CharField ('numero de contacto',max_length=25,blank=True)
    Correo = models.EmailField('Correo', blank=True)
    Hora = models.CharField('Hora de atencion',max_length=300)
    Direccion = models.CharField(max_length=300)
    DetalleProblema = models.CharField('Detalle del problema',max_length=300) 
    ImagenProblema = models.ImageField('Imagen del problema',null=True, blank=True, upload_to="img/")
    
    def __str__(self):
      return self.Nombre