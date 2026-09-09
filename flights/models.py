from django.db import models


class Flight(models.Model):

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("active", "Active"),
        ("landed", "Landed"),
        ("cancelled", "Cancelled"),
        ("incident", "Incident"),
        ("unknown", "Unknown"),
    ]

    # ==============================
    # BASIC FLIGHT INFORMATION
    # ==============================

    flight_date = models.DateField(
        blank=True,
        null=True
    )

    flight_status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="unknown",
        db_index=True
    )

    flight_number = models.CharField(
        max_length=20,
        db_index=True
    )

    flight_iata = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        db_index=True
    )

    flight_icao = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    callsign = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    # ==============================
    # AIRLINE
    # ==============================

    airline_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    airline_iata = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    airline_icao = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    # ==============================
    # DEPARTURE
    # ==============================

    departure_airport = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    departure_timezone = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    departure_iata = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    departure_icao = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    departure_terminal = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    departure_gate = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    departure_delay = models.IntegerField(
        blank=True,
        null=True
    )

    departure_scheduled = models.DateTimeField(
        blank=True,
        null=True
    )

    departure_estimated = models.DateTimeField(
        blank=True,
        null=True
    )

    departure_actual = models.DateTimeField(
        blank=True,
        null=True
    )

    departure_estimated_runway = models.DateTimeField(
        blank=True,
        null=True
    )

    departure_actual_runway = models.DateTimeField(
        blank=True,
        null=True
    )

    # ==============================
    # ARRIVAL
    # ==============================

    arrival_airport = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    arrival_timezone = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    arrival_iata = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    arrival_icao = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    arrival_terminal = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    arrival_gate = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    arrival_baggage = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    arrival_delay = models.IntegerField(
        blank=True,
        null=True
    )

    arrival_scheduled = models.DateTimeField(
        blank=True,
        null=True
    )

    arrival_estimated = models.DateTimeField(
        blank=True,
        null=True
    )

    arrival_actual = models.DateTimeField(
        blank=True,
        null=True
    )

    arrival_estimated_runway = models.DateTimeField(
        blank=True,
        null=True
    )

    arrival_actual_runway = models.DateTimeField(
        blank=True,
        null=True
    )

    # ==============================
    # AIRCRAFT
    # ==============================

    aircraft_registration = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    aircraft_iata = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    aircraft_icao = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    aircraft_icao24 = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    # ==============================
    # LIVE POSITION
    # ==============================

    latitude = models.FloatField(
        blank=True,
        null=True
    )

    longitude = models.FloatField(
        blank=True,
        null=True
    )

    altitude = models.FloatField(
        blank=True,
        null=True
    )

    direction = models.FloatField(
        blank=True,
        null=True
    )

    speed_horizontal = models.FloatField(
        blank=True,
        null=True
    )

    speed_vertical = models.FloatField(
        blank=True,
        null=True
    )

    # ==============================
    # SYSTEM INFORMATION
    # ==============================

    data_source = models.CharField(
        max_length=50,
        default="aviationstack"
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.flight_iata or self.flight_number