from django.urls import path
from .viewsets import UserViewSet, ShowViewSet, TicketViewSet, SeatViewSet,MovieViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'shows', ShowViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls
urlpatterns = [
        path('auth/', obtain_auth_token, name='auth'),

] + router.urls
