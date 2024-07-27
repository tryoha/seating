from django.db import models


class Place(models.Model):
    place = models.CharField(max_length=60, unique=True)
    max_seats = models.PositiveIntegerField()

    def __str__(self):
        return self.place


class Seat(models.Model):
    seat = models.PositiveIntegerField(unique=True)
    available = models.BooleanField(default=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="seats")

    def __str__(self):
        return str(self.seat)

    class Meta:
        ordering = ["seat"]
