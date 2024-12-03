"""
Konfigurace WSGI pro projekt mysite.

Zpřístupňuje WSGI, které lze volat jako proměnnou na úrovni modulu s názvem ,,application''.

Další informace o tomto souboru naleznete v části
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
