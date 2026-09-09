from flights.models import Flight


def get_flight(flight_iata):
    """Find a specific flight."""
    return Flight.objects.filter(
        flight_iata__iexact=flight_iata
    ).first()


def get_delayed_flights():
    """Return flights with a reported arrival or departure delay."""
    return Flight.objects.filter(
        arrival_delay__gt=0
    ) | Flight.objects.filter(
        departure_delay__gt=0
    )


def get_active_flights():
    """Return currently active flights."""
    return Flight.objects.filter(
        flight_status="active"
    )


def get_scheduled_flights():
    """Return scheduled flights."""
    return Flight.objects.filter(
        flight_status="scheduled"
    )


def get_cancelled_flights():
    """Return cancelled flights."""
    return Flight.objects.filter(
        flight_status="cancelled"
    )


def get_airline_flights(airline_name):
    """Return flights belonging to an airline."""
    return Flight.objects.filter(
        airline_name__icontains=airline_name
    )


def get_departure_flights(airport):
    """Return flights departing from an airport."""
    return Flight.objects.filter(
        departure_iata__iexact=airport
    )


def get_arrival_flights(airport):
    """Return flights arriving at an airport."""
    return Flight.objects.filter(
        arrival_iata__iexact=airport
    )


def format_flight(flight):
    """Convert a Flight object into readable information."""

    return {
        "flight": flight.flight_iata,
        "flight_number": flight.flight_number,
        "airline": flight.airline_name,
        "date": str(flight.flight_date),
        "status": flight.flight_status,

        "departure": {
            "airport": flight.departure_airport,
            "iata": flight.departure_iata,
            "terminal": flight.departure_terminal,
            "gate": flight.departure_gate,
            "delay": flight.departure_delay,
            "scheduled": str(flight.departure_scheduled),
            "estimated": str(flight.departure_estimated),
            "actual": str(flight.departure_actual),
        },

        "arrival": {
            "airport": flight.arrival_airport,
            "iata": flight.arrival_iata,
            "terminal": flight.arrival_terminal,
            "gate": flight.arrival_gate,
            "baggage": flight.arrival_baggage,
            "delay": flight.arrival_delay,
            "scheduled": str(flight.arrival_scheduled),
            "estimated": str(flight.arrival_estimated),
            "actual": str(flight.arrival_actual),
        },

        "aircraft": {
            "registration": flight.aircraft_registration,
            "iata": flight.aircraft_iata,
            "icao": flight.aircraft_icao,
            "icao24": flight.aircraft_icao24,
        },
    }


def format_flight_list(flights):
    """Convert multiple flights into readable information."""

    return [
        format_flight(flight)
        for flight in flights
    ]