from django.urls import path

from .views import argo_index, liner_index

app_name = "seats"

urlpatterns = [
    path("", argo_index, name="main"),
    path("argo/", argo_index, name="argo"),
    path("liner/", liner_index, name="liner"),
]
