from dataclasses import field, fields
from django import forms




class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control"
                }
            )
        )
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
                }
            )
        )