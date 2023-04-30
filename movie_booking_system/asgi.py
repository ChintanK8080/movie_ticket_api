import os

from django.core.asgi import get_asgi_application
#for web socket
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import home.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_booking_system.settings')

# for web socket
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(home.routing.websocket_urlpatterns)
    )
})
