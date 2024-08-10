from django.contrib import admin

from .models import Place, Seat


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "available")
    list_editable = ("available",)
    list_filter = ("available",)
    search_fields = ("name",)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat", "place", "available")
    list_editable = ("available",)
    list_filter = ("available", "place")
    search_fields = ("seat",)
