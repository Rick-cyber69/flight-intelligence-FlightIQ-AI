from .flight_tools import (
    get_flight,
    get_delayed_flights,
    get_active_flights,
    get_scheduled_flights,
    get_cancelled_flights,
    get_airline_flights,
    get_departure_flights,
    get_arrival_flights,
    format_flight,
    format_flight_list,
)


def dispatch_flight_query(intent_data):

    intent = intent_data.get("intent")
    flight_iata = intent_data.get("flight_iata")
    airline_name = intent_data.get("airline_name")
    airport_iata = intent_data.get("airport_iata")
    airport_name = intent_data.get("airport_name")

    # --------------------------------------------------
    # Specific flight
    # --------------------------------------------------

    if intent == "flight_details":

        if not flight_iata:
            return {
                "type": "error",
                "message": "No specific flight number was identified."
            }

        flight = get_flight(flight_iata)

        if not flight:
            return {
                "type": "not_found",
                "message": f"Flight {flight_iata} was not found in the database."
            }

        return {
            "type": "flight",
            "data": format_flight(flight)
        }

    # --------------------------------------------------
    # Delayed flights
    # --------------------------------------------------

    if intent == "delayed_flights":

        flights = get_delayed_flights()

        if airline_name:
            flights = flights.filter(
                airline_name__icontains=airline_name
            )

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Active flights
    # --------------------------------------------------

    if intent == "active_flights":

        flights = get_active_flights()

        if airline_name:
            flights = flights.filter(
                airline_name__icontains=airline_name
            )

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Scheduled flights
    # --------------------------------------------------

    if intent == "scheduled_flights":

        flights = get_scheduled_flights()

        if airline_name:
            flights = flights.filter(
                airline_name__icontains=airline_name
            )

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Cancelled flights
    # --------------------------------------------------

    if intent == "cancelled_flights":

        flights = get_cancelled_flights()

        if airline_name:
            flights = flights.filter(
                airline_name__icontains=airline_name
            )

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Airline flights
    # --------------------------------------------------

    if intent == "airline_flights":

        if not airline_name:
            return {
                "type": "error",
                "message": "No airline was identified."
            }

        flights = get_airline_flights(airline_name)

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Departure flights
    # --------------------------------------------------

    if intent == "departure_flights":

        if airport_iata:
            flights = get_departure_flights(airport_iata)

        elif airport_name:
            from flights.models import Flight

            flights = Flight.objects.filter(
                departure_airport__icontains=airport_name
            )

        else:
            return {
                "type": "error",
                "message": "No departure airport was identified."
            }

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Arrival flights
    # --------------------------------------------------

    if intent == "arrival_flights":

        if airport_iata:
            flights = get_arrival_flights(airport_iata)

        elif airport_name:
            from flights.models import Flight

            flights = Flight.objects.filter(
                arrival_airport__icontains=airport_name
            )

        else:
            return {
                "type": "error",
                "message": "No arrival airport was identified."
            }

        return {
            "type": "flight_list",
            "intent": intent,
            "count": flights.count(),
            "data": format_flight_list(flights)
        }

    # --------------------------------------------------
    # Unknown
    # --------------------------------------------------

    return {
        "type": "unknown",
        "message": "I could not determine the required flight search."
    }