from django.urls import path

from .views import romantic_index

app_name = "seats"

urlpatterns = [
    path("", romantic_index, name="main"),
]
