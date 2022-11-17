from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from apps.direccion.models import Direccion

# Create your models here.

#Creacion de la clase manager para creacion de dos tipos de usuarios
class UsuarioManager(BaseUserManager):
    #Usuario normal
    def create_user(self,email,username,nombres,apellidoP,apellidoM,password = None):
        if not email:
            raise ValueError('El usuario debe contar con un correo electronico...')
       
        usuario = self.model(
            email =self.normalize_email(email),
            username = username,
            nombres = nombres,
            apellidoP = apellidoP,
            apellidoM = apellidoM,
            

        )
        #Encriptación de la contraseña
        Usuario.set_password(password)
        #Guardado
        Usuario.save()
        return usuario
    #Usuario administrador
    def create_superuser(self,email,username,nombres,apellidoP,apellidoM,password):
        Usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            password = password,
            apellidoP = apellidoP,
            apellidoM = apellidoM,

        )
        #Cambio a administrador
        Usuario.Usuario_administrator = True
        #Guardado
        Usuario.save()
        return Usuario
        
        
class Usuario(AbstractBaseUser):
    #Define los campos de la BD del usuario de forma personalizada
    id = models.AutoField(primary_key = True)
    email= models.EmailField("Correo electronico", max_length=254, unique = True)
    username=models.CharField('Nombre de usuario',unique = True, max_length = 50)
    nombres=models.CharField('Nombre', max_length = 50)
    apellidoP=models.CharField('Apellido paterno', max_length = 50)
    apellidoM=models.CharField('Apellido materno', max_length = 50)
    FecNac=models.DateField(blank = True, null = True)
    dir_id=models.ForeignKey(Direccion, on_delete=models.CASCADE,null = True)
    Usuario_activo=models.BooleanField('Está activo',default = True)
    Usuario_administrator=models.BooleanField('Administrador',default = False)
    Usuario_engineer=models.BooleanField('Ingeniero',default = False)
    #Creacion de administrador a través del manager
    objects = UsuarioManager()
    #Campos requeriods para el inicio de sesion y de registro
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nombres', 'apellidoP', 'apellidoM']
    
    def __str__(self):
        return f'{self.nombres},{self.apellidoP}'
    #Permisos de administrador de django
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    #-----------------------------------
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    def __str__(self):
        return self.nombres,self.apellidoP,self.apellidoM
    
    @property
    def is_staff(self):
        return self.Usuario_administrator