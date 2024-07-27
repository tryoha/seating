from django.urls import path

from .views import index

app_name = "seats"

urlpatterns = [
    path("", index, name="index"),
]
