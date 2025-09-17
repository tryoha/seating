from django.db.models.manager import BaseManager
from django.shortcuts import render

from .models import Place, Seat


def index(request):
    places = Place.objects.all()
    return render(request, "seats/index.html", {"places": places})


def argo_index(request):
    places = Place.objects.filter(available=True)
    seats = Seat.objects.filter(place__name="Арго")
    context: dict[str, BaseManager[Place]] = {"places": places}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/argo.html", context)


def liner_index(request):
    places = Place.objects.filter(available=True)
    seats = Seat.objects.filter(place__name="Лайнер")
    context: dict[str, BaseManager[Place]] = {"places": places}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/liner.html", context)

