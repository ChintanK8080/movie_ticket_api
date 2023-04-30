from django.contrib import admin
from django.urls import path, include
from home import urls ,routing
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(urls)),
    path('admin/', admin.site.urls),
    path('ws/', include(routing.websocket_urlpatterns)),

]
# for image root
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)