from dataclasses import field
from pyexpat import model
from django import forms

from apps.usuario.models import Usuario


class FormularioUsuario(forms.ModelForm):
    password1 = forms.CharField(
        label = "Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Crear contraseña",
                "id":"password1",
                "required":"required",
            }
        )
    )
    password2 = forms.CharField(
        label = "Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirmar contraseña",
                "id":"password2",
                "required":"required",
            }
        )
    )
    class Meta:
        model = Usuario
        fields = ('username', 'nombres', 'apellidoP', 'apellidoM', 'email', 'FecNac',
                  'dir_id', 'Usuario_activo', 'Usuario_administrator', 'Usuario_engineer')
        labels = {
            'username': 'Usuario',
            'nombres': 'Nombre',
            'apellidoP': 'Apellido Paterno',
            'apellidoM': 'Apellido Materno',
            'email': 'Correo Electronico',
            'FecNac': 'Fecha de nacimiento',
            'dir_id': 'Dirección',
            'Usuario_activo': 'Activo',
            'Usuario_administrator': 'Administrador',
            'Usuario_engineer': 'Ingeniero',
        }
        widgets = { 
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Usuario',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Nombre',
                }
            ),
            'apellidoP': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Apellido Paterno',
                }
            ),
            'apellidoM': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Apellido Materno',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'E-mail',
                }
            ),
            'FecNac': forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'DD/MM/YYYY',
                }
            ),
        }
    def clean_password2(self):
        """
        Validacion de contrasena
        
        Metodo que valida que ambas contrasenas ingresadas sean igual, 
        esto antes de ser encriptadas y guardadas en la base de datos
        
        Exception:
        -ValidationError
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')      
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contrasenas no coinciden')  
        return password2
        """Guardado de la contrasena, despues de la validacion se comprueba que siga en proceso
        si el resultado es positivo entonces guarda la contrasena y retorna al usuario
        sino limpia el campo normalizandolo a un formato consistente
        """
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user