from django.db import models


class Place(models.Model):
    place = models.CharField("Название ресторана", max_length=60, unique=True)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class Seat(models.Model):
    seat = models.PositiveIntegerField("Место", unique=True)
    available = models.BooleanField("Доступность", default=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="seats")

    def __str__(self):
        return str(self.seat)

    class Meta:
        ordering = ["seat"]
        verbose_name = "Место"
        verbose_name_plural = "Места"
