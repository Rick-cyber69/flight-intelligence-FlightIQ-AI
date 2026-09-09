from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.flight_search,
        name="flight_search"
    ),

    path(
        "flight/<str:flight_iata>/",
        views.flight_detail,
        name="flight_detail"
    ),
]