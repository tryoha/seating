from typing import Literal

from django.contrib import admin

from .models import Place, Seat


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("place", "max_seats")


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat", "place", "available")
    list_editable = ("available",)
