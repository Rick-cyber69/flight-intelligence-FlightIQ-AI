from django.contrib import admin
from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):

    list_display = (
        "flight_iata",
        "flight_number",
        "airline_name",
        "departure_iata",
        "arrival_iata",
        "flight_status",
        "last_updated",
    )

    search_fields = (
        "flight_iata",
        "flight_number",
        "flight_icao",
        "airline_name",
        "departure_iata",
        "arrival_iata",
    )

    list_filter = (
        "flight_status",
        "airline_name",
        "departure_iata",
        "arrival_iata",
    )

    readonly_fields = (
        "last_updated",
        "created_at",
    )