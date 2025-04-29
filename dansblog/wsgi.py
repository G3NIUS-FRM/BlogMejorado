"""
WSGI config for dansblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dansblog.settings')

application = get_wsgi_application()

#Para que el servidor pueda reconocer como va a iniciar la pagina
app=application