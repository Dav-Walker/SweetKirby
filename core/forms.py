from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Ingrese un correo electrónico válido.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Email',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {
            'username': 'Mínimo 6 caracteres. Únicamente letras.',
            'password1': 'Su contraseña no puede asemejarse tanto a su otra información personal. Debe contener al menos 8 caracteres. No puede ser una clave utilizada comúnmente. No puede ser completamente numérica.',
            'password2': 'Para verificar, introduzca la misma contraseña anterior.',
        }
