from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginForm

from apps.usuario.models import Usuario


def login_user (request):
    formset = LoginForm(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request,email=email,password=password)
            if user is not None and Usuario.Usuario_administrator:
                login(request,user)
                return redirect('/Admin/home/')
            elif user is not None :
                login(request,user)
                return redirect('/home/menu/')
            else:
                messages.success(request,('Hubo un error al intentar iniciar sesión, intentalo nuevamente...'))
                return redirect('/members/login/')        
    return render(request,'authentication/login.html',{'formset':formset})

def logout_view(request):
    logout(request)
    return redirect('/members/login/') 