from rest_framework import viewsets
from .models import User, Show, Ticket, Seat,Movie
from .serializers import UserSerializer, ShowSerializer, TicketSerializer, SeatSerializer,MovieSerializer
from rest_framework.permissions import IsAuthenticated
from .authentication import UserAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [UserAuthentication]
    permission_classes = [IsAuthenticated]
class ShowViewSet(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
