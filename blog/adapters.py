#Clase para el adapter de cuentas sociales como google
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
#Una excepcion para poder sacar un error 
from allauth.core.exceptions import ImmediateHttpResponse
#Para devolver Error y mandar al sistema un status 400
from django.http import HttpResponse

#Para devolver el modelo de usuario que esta en settings AUTH_USER_MODEL
from django.contrib.auth import get_user_model

#Cargando modelo
User = get_user_model()

'''
Esta Clase la estoy utilizando para poder verificar
que los usuarios no puedan registrar el mismo email
de google
'''

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    
    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            return
        # Verifica si ya existe un usuario con ese email
        email = sociallogin.account.extra_data.get('email')
        if email and User.objects.filter(email=email).exists():
            # Si existe, lanza un error o redirige
            raise ImmediateHttpResponse(HttpResponse(
                "Ya existe una cuenta registrada con ese correo. Intenta iniciar sesión.", status=400
            ))