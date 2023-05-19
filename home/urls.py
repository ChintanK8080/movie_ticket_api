from django.urls import path
from .viewsets import  ShowViewSet, TicketViewSet, SeatViewSet,MovieViewSet,RegisterAPI
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views
from .viewsets import LoginAPI


router = DefaultRouter()
router.register(r'api/shows', ShowViewSet)
router.register(r'api/tickets', TicketViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/movies', MovieViewSet)

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

        
]

urlpatterns += router.urls
