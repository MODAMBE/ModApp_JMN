import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModApp.settings')

# L'application ASGI HTTP
django_asgi_app = get_asgi_application()

# Import du routing **après** que Django soit prêt
from eglise import routing as eglise_routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                eglise_routing.websocket_urlpatterns
            )
        )
    ),
})
