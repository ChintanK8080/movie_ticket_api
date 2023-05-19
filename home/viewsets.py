from rest_framework import viewsets,response,status,generics, permissions
from .models import  Show, Ticket, Seat,Movie
from .serializers import  ShowSerializer, TicketSerializer, SeatSerializer,MovieSerializer,UserSerializer, RegisterSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import IsAuthenticated







class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class ShowViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class SeatViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
