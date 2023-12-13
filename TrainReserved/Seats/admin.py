from django.contrib import admin
from .models import Train, Seats

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_number', 'departure_station', 'arrival_station', 'departure_time', 'arrival_time', 'total_seats')
    search_fields = ['train_number', 'departure_station', 'arrival_station']
    list_filter = ['departure_time', 'arrival_time']

@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ('train', 'seat_number', 'is_booked')
    search_fields = ['train__train_number', 'seat_number']
    list_filter = ['is_booked']

