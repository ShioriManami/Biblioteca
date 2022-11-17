from pathlib import Path
from django.contrib import admin
from django.urls import path,include 
from django.contrib.auth import logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/',include(('apps.usuario.urls','Account'))),
    path('Admin/',include(('apps.Administrador.urls','Admin'))),
]
