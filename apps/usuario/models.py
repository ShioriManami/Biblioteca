from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.direccion.models import Direccion

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidoP,apellidoM,password = None):
        if not email:
            raise ValueError('El usuario debe contar con un correo electronico...')
       
        Usuario = self.model(
            email =self.normalize_email(email),
            username = username,
            nombres = nombres,
            apellidoP = apellidoP,
            apellidoM = apellidoM,
            
            #FecNac = FecNac,
            #dir_id = dir_id
        )
        Usuario.set_password(password)
        Usuario.save()
        return Usuario
        
    def create_superuser(self,email,username,nombres,apellidoP,apellidoM,password):
        Usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            password = password,
            apellidoP = apellidoP,
            apellidoM = apellidoM,
            #FecNac = FecNac,
            #dir_id = dir_id
        )
        Usuario.Usuario_administrador = True
        Usuario.save()
        return Usuario
        
        
class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key = True)
    username=models.CharField('Nombre de usuario',unique = True, max_length = 50)
    nombres=models.CharField('Nombre', max_length = 50)
    apellidoP=models.CharField('Apellido paterno', max_length = 50)
    apellidoM=models.CharField('Apellido materno', max_length = 50)
    FecNac=models.DateField(blank = True, null = True)
    dir_id=models.ForeignKey(Direccion, on_delete=models.CASCADE,null = True)
    Usuario_activo=models.BooleanField(default = True)
    Usuario_administrador=models.BooleanField(default = False)
    email= models.EmailField("Correo electronico", max_length=254, unique = True)
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombres', 'apellidoP', 'apellidoM']
    
    def __str__(self):
        return f'{self.username},{self.apellidoP}'
    
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return self.nombres
    
    @property
    def is_staff(self):
        return self.Usuario_administrador