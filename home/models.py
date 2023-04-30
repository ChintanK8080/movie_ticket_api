from django.db import models
from django.core.validators import MaxValueValidator


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.user_name

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_image = models.ImageField(upload_to='movies_posters/')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name    

class Show(models.Model):
    show_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    time_started = models.DateTimeField()
    time_ended = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(f"{self.movie_id.name} ({self.time_started.strftime('%d-%b %H:%M')}-{self.time_ended.strftime('%H:%M')})")

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)  
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return str(self.ticket_id)

class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    seat_number = models.IntegerField(validators=[MaxValueValidator(300)],null=False,default=0)

    def __str__(self):
        return str(self.seat_id)
