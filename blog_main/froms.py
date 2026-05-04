from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # passowrd1 es el campo para la contraseña y password2 es para confirmar la contraseña.
        fields= ('email', 'username', 'password1', 'password2')
        