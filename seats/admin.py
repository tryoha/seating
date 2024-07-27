from django.contrib import admin

from .models import Place, Seat


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("place",)


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat", "place", "available")
    list_editable = ("available",)
    list_filter = ("available", "place")
    search_fields = ("seat",)

    def place(self, obj):
        return obj.place
