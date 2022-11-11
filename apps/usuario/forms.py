from django import forms
from django.contrib.auth.forms import AuthenticationForm
from apps.usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña' 
class FormularioUsuario(forms.ModelForm):
    
    password1 = forms.CharField(label = 'contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'from-control',
            'placeholder':'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))
    
    password2 = forms.CharField( label = 'contraseña de confirmación', widget=forms.PasswordInput(
        attrs = {
            'class' : 'from-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
        ))