from django.urls import path

from .views import minvody_index

app_name = "seats"

urlpatterns = [
    path("", minvody_index, name="main"),
    path("minvody/", minvody_index, name="minvody"),
]
