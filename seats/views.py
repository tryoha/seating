from django.shortcuts import render

from .models import Seat


def index(request):
    seats = Seat.objects.all()
    context = {}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/index.html", context)
