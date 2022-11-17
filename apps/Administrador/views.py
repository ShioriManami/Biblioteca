from django.shortcuts import render, redirect
from django.views.generic import ListView,FormView,TemplateView,CreateView,DeleteView

from django.urls import reverse_lazy
from . import views
from .forms import FormularioUsuario
from apps.usuario.models import Usuario

from apps.usuario.models import Usuario

# Create your views here.

class home(TemplateView):
    template_name = "AdminHome.html"


class ListaUsuarios(ListView):
    model = Usuario
    template_name = "AdminUsuarioLista.html"
    queryset: Usuario.objects.all()
"""
class CrearUsuarios(CreateView):
    model: Usuario
    form_class= UserRegisterForm
    template_name = "CreateUser.html"
    success_url: reverse_lazy(views.ListaUsuarios)
"""
class EditarUsuarios(FormView):
    model: Usuario

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = "CreateUser.html"
    success_url: reverse_lazy('Admin:ListaUsuarios')
