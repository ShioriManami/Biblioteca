from django.db import models
from apps.direccion.models import Direccion

# Create your models here.
class Sitios(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de sitio', max_length = 50, blank = False, null = False)
    Red = models.CharField('Nombre de red', max_length = 50, blank = False, null = False)
    dir_id=models.ForeignKey(Direccion, on_delete=models.CASCADE,null = True)
    Enlace = models.CharField('Numero de enlace', max_length = 10, blank = False, null = False)
    punta = models.CharField('Punta (A/B)', max_length = 10, blank = False, null = False)
    
    class Meta:
        verbose_name = 'Sitio'
        verbose_name_plural = 'Sitios'
        
    def __str__(self):
        return self.nombre
    