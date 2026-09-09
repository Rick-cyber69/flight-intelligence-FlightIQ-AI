from .api_client import AviationStackClient
from .models import Flight


def search_flight(flight_number):
    """
    Search Aviationstack for a specific flight.
    """

    client = AviationStackClient()

    response = client.get_flights(
        flight_iata=flight_number
    )

    return response


def save_flight(data):
    """
    Save or update a flight returned by Aviationstack.
    """

    flights = data.get("data", [])

    if not flights:
        return None

    item = flights[0]

    departure = item.get("departure") or {}
    arrival = item.get("arrival") or {}
    airline = item.get("airline") or {}
    flight = item.get("flight") or {}
    aircraft = item.get("aircraft") or {}
    live = item.get("live") or {}

    flight_iata = flight.get("iata")

    if not flight_iata:
        return None

    flight_object, created = Flight.objects.update_or_create(
        flight_iata=flight_iata,
        defaults={
            # -----------------------------
            # BASIC FLIGHT INFORMATION
            # -----------------------------

            "flight_date": item.get("flight_date"),

            "flight_status": item.get(
                "flight_status",
                "unknown"
            ),

            "flight_number": flight.get("number"),

            "flight_icao": flight.get("icao"),

            "callsign": flight.get("callsign"),

            # -----------------------------
            # AIRLINE
            # -----------------------------

            "airline_name": airline.get("name"),

            "airline_iata": airline.get("iata"),

            "airline_icao": airline.get("icao"),

            # -----------------------------
            # DEPARTURE
            # -----------------------------

            "departure_airport": departure.get(
                "airport"
            ),

            "departure_timezone": departure.get(
                "timezone"
            ),

            "departure_iata": departure.get(
                "iata"
            ),

            "departure_icao": departure.get(
                "icao"
            ),

            "departure_terminal": departure.get(
                "terminal"
            ),

            "departure_gate": departure.get(
                "gate"
            ),

            "departure_delay": departure.get(
                "delay"
            ),

            "departure_scheduled": departure.get(
                "scheduled"
            ),

            "departure_estimated": departure.get(
                "estimated"
            ),

            "departure_actual": departure.get(
                "actual"
            ),

            "departure_estimated_runway": departure.get(
                "estimated_runway"
            ),

            "departure_actual_runway": departure.get(
                "actual_runway"
            ),

            # -----------------------------
            # ARRIVAL
            # -----------------------------

            "arrival_airport": arrival.get(
                "airport"
            ),

            "arrival_timezone": arrival.get(
                "timezone"
            ),

            "arrival_iata": arrival.get(
                "iata"
            ),

            "arrival_icao": arrival.get(
                "icao"
            ),

            "arrival_terminal": arrival.get(
                "terminal"
            ),

            "arrival_gate": arrival.get(
                "gate"
            ),

            "arrival_baggage": arrival.get(
                "baggage"
            ),

            "arrival_delay": arrival.get(
                "delay"
            ),

            "arrival_scheduled": arrival.get(
                "scheduled"
            ),

            "arrival_estimated": arrival.get(
                "estimated"
            ),

            "arrival_actual": arrival.get(
                "actual"
            ),

            "arrival_estimated_runway": arrival.get(
                "estimated_runway"
            ),

            "arrival_actual_runway": arrival.get(
                "actual_runway"
            ),

            # -----------------------------
            # AIRCRAFT
            # -----------------------------

            "aircraft_registration": aircraft.get(
                "registration"
            ),

            "aircraft_iata": aircraft.get(
                "iata"
            ),

            "aircraft_icao": aircraft.get(
                "icao"
            ),

            "aircraft_icao24": aircraft.get(
                "icao24"
            ),

            # -----------------------------
            # LIVE POSITION
            # -----------------------------

            "latitude": live.get(
                "latitude"
            ),

            "longitude": live.get(
                "longitude"
            ),

            "altitude": live.get(
                "altitude"
            ),

            "direction": live.get(
                "direction"
            ),

            "speed_horizontal": live.get(
                "speed_horizontal"
            ),

            "speed_vertical": live.get(
                "speed_vertical"
            ),
        }
    )

    return flight_object, created