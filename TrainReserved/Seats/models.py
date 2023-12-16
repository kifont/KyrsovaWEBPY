from django.db import models


class Train(models.Model):
    train_number = models.CharField(max_length=10, unique=True, help_text="Номер поїзда")
    departure_station = models.CharField(max_length=100, help_text="Станція відправлення")
    arrival_station = models.CharField(max_length=100, help_text="Станція призначення")
    departure_time = models.DateTimeField(help_text="Час відправлення")
    arrival_time = models.DateTimeField(help_text="Час прибуття")
    total_seats = models.PositiveIntegerField(help_text="Загальна кількість місць у поїзді")

    def __str__(self):
        return f"{self.train_number} - {self.departure_station} to {self.arrival_station}"
class Seats(models.Model):

    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='seats', help_text="Поїзд")
    seat_number = models.CharField(max_length=5, help_text="Номер місця")
    is_booked = models.BooleanField(default=False, help_text="Статус бронювання")

    def __str__(self):
        return f"Seat {self.seat_number} in Train {self.train.train_number}"




