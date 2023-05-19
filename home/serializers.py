from rest_framework import serializers
from .models import  Show, Ticket, Seat,Movie
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id','movie_image','name','description')




class ShowSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True,source = 'movie_id')

    class Meta:
        model = Show
        fields = ('show_id', 'time_started', 'time_ended','price','movie')

class TicketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, source='id')
    show = ShowSerializer(read_only=True, source='show_id')

    class Meta:
        model = Ticket
        fields = ('ticket_id', 'user', 'show', 'is_booked')

class SeatSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True,source='id')
    show = ShowSerializer(read_only=True,source='show_id')
    class Meta:
        model = Seat
        fields = ('seat_id', 'show_id','show','user')

