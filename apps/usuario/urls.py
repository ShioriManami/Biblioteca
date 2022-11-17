from django.urls import path
from .views import login_user,logout_view

urlpatterns = [
    path('login/',login_user,name='auth'),
    path('logout/',logout_view,name='logout'),
]
