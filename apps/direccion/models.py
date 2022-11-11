from django.db import models


# Create your models here.
class Direccion(models.Model):
    id = models.AutoField(primary_key = True)
    Pais = models.CharField('Pais', max_length = 50, blank = False, null = False)
    Estado = models.CharField('Estado', max_length = 50, blank = False, null = False)
    Municipio = models.CharField('Municipio', max_length = 30, blank = False, null = False)
    Ciudad = models.CharField('Ciudad', max_length = 30, blank = False, null = False)
    Colonia = models.CharField('Colonia', max_length = 50, blank = False, null = False)
    Calle = models.CharField('Calle', max_length = 30, blank = False, null = False)
    Numero = models.IntegerField(blank = False, null = False)


    class Meta:
        verbose_name = 'Direccion'
        verbose_name_plural = 'Direcciones'
        
    def __str__(self):
        return self.Municipio