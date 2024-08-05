from django.db import models


class Place(models.Model):
    name = models.CharField("Название ресторана", max_length=60, unique=True)

    def __str__(self):  # -> Any:
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class Seat(models.Model):
    seat = models.PositiveIntegerField("Место")
    available = models.BooleanField("Доступность", default=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="seats")

    def __str__(self):
        return str(self.seat)

    class Meta:
        ordering = ["seat"]
        verbose_name = "Место"
        verbose_name_plural = "Места"
