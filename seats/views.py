from django.shortcuts import render

from .models import Place, Seat


def index(request):
    places = Place.objects.all()
    return render(request, "seats/index.html", {"places": places})


def ballroom_index(request):
    seats = Seat.objects.filter(place__name="ballroom")
    context = {}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/ballroom.html", context)


def grilled_index(request):
    seats = Seat.objects.filter(place__name="grilled")
    context = {}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/grilled.html", context)


def mangup_index(request):
    seats = Seat.objects.filter(place__name="mangup")
    context = {}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/mangup.html", context)


def tavrika_index(request):
    seats = Seat.objects.filter(place__name="tavrika")
    context = {}

    for seat in seats:
        context[seat.seat] = {"place": seat.place, "available": seat.available}

    return render(request, "seats/tavrika.html", context)
