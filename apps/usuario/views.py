from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.views.generic import TemplateView


def login_user (request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('Hubo un error al intentar iniciar, intentalo nuevamente...'))
            return redirect(login)
    else:
        return render(request, 'index.html',{})
    
class Index(TemplateView):
    template_name = "index.html"
