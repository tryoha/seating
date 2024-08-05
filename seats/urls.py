from django.urls import path

from .views import ballroom_index, grilled_index, index, mangup_index, tavrika_index

app_name = "seats"

urlpatterns = [
    path("", ballroom_index, name="main"),
    path("ballroom/", ballroom_index, name="ballroom"),
    path("grilled/", grilled_index, name="grilled"),
    path("mangup/", mangup_index, name="mangup"),
    path("tavrika/", tavrika_index, name="tavrika"),
]
