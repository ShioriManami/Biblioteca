from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

# Creacion de urls para administrador

urlpatterns = [
    path('home/',login_required(views.home.as_view()),name='home'),
    
    path('Lista_Usuarios/', login_required(views.ListaUsuarios.as_view()), name='ListaUsuarios'),
    path('Crear_Usuario/', login_required(views.RegistrarUsuario.as_view()), name='CrearUsuario'),
    path('Editar_Usuario/<int:pk>/', login_required(views.ListaUsuarios.as_view()), name='EditarUsuario'),
    path('Eliminar_Usuario/<int:pk>/', login_required(views.ListaUsuarios.as_view()), name='EliminarUsuario'),
]
