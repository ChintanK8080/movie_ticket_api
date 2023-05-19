from django.contrib import admin
from .models import  Show, Ticket, Seat,Movie

admin.site.register(Show)
admin.site.register(Ticket)
admin.site.register(Seat)
admin.site.register(Movie)
