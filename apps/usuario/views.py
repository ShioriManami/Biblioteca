from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def login_user (request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('Hubo un error al intentar iniciar sesión, intentalo nuevamente...'))
            return redirect('auth')
    else:
        return render(request,'authentication/login.html',{})
