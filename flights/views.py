from django.shortcuts import render, get_object_or_404

from .models import Flight, FlightSearchHistory
from .services import search_flight, save_flight


def flight_search(request):

    flight_number = request.GET.get(
        "flight",
        ""
    ).strip().upper()

    flights = Flight.objects.none()

    searched = False
    error = None

    if flight_number:

        searched = True

        # ================================================
        # LOGGED-IN USER
        # ================================================

        if request.user.is_authenticated:

            # Search database first
            flights = Flight.objects.filter(
                flight_iata__icontains=flight_number
            )

            # If not found, retrieve from Aviationstack
            if not flights.exists():

                try:

                    result = search_flight(
                        flight_number
                    )

                    if result.get("data"):

                        flight, created = save_flight(
                            result
                        )

                        flights = Flight.objects.filter(
                            id=flight.id
                        )

                    else:

                        error = (
                            "No flight information was found."
                        )

                except Exception as e:

                    error = str(e)

            # Save search history
            if flights.exists():

                for flight in flights:

                    FlightSearchHistory.objects.create(
                        user=request.user,
                        flight=flight
                    )

        # ================================================
        # GUEST USER
        # ================================================

        else:

            try:

                # Get flight directly from Aviationstack.
                # DO NOT save it to SQLite.

                result = search_flight(
                    flight_number
                )

                if result.get("data"):

                    # Temporary object for template display.
                    # Nothing is written to the database.

                    item = result["data"][0]

                    departure = item.get("departure") or {}
                    arrival = item.get("arrival") or {}
                    airline = item.get("airline") or {}
                    flight_data = item.get("flight") or {}
                    aircraft = item.get("aircraft") or {}

                    guest_flight = {
                        "flight_iata": flight_data.get("iata"),
                        "flight_number": flight_data.get("number"),
                        "flight_icao": flight_data.get("icao"),
                        "flight_status": item.get(
                            "flight_status",
                            "unknown"
                        ),

                        "airline_name": airline.get("name"),

                        "departure_iata": departure.get("iata"),
                        "departure_airport": departure.get("airport"),
                        "departure_terminal": departure.get("terminal"),
                        "departure_gate": departure.get("gate"),
                        "departure_delay": departure.get("delay"),
                        "departure_scheduled": departure.get("scheduled"),
                        "departure_estimated": departure.get("estimated"),
                        "departure_actual": departure.get("actual"),

                        "arrival_iata": arrival.get("iata"),
                        "arrival_airport": arrival.get("airport"),
                        "arrival_terminal": arrival.get("terminal"),
                        "arrival_gate": arrival.get("gate"),
                        "arrival_baggage": arrival.get("baggage"),
                        "arrival_delay": arrival.get("delay"),
                        "arrival_scheduled": arrival.get("scheduled"),
                        "arrival_estimated": arrival.get("estimated"),
                        "arrival_actual": arrival.get("actual"),

                        "aircraft_registration": aircraft.get(
                            "registration"
                        ),
                        "aircraft_iata": aircraft.get("iata"),
                        "aircraft_icao": aircraft.get("icao"),
                        "aircraft_icao24": aircraft.get("icao24"),
                    }

                    # Template expects a collection
                    flights = [guest_flight]

                else:

                    error = (
                        "No flight information was found."
                    )

            except Exception as e:

                error = str(e)

    context = {
        "flights": flights,
        "searched": searched,
        "error": error,
        "flight_number": flight_number,
    }

    return render(
        request,
        "flights/flight_search.html",
        context
    )


def flight_detail(request, flight_iata):

    # ----------------------------------------------------
    # Logged-in users can use database flight details
    # ----------------------------------------------------

    if request.user.is_authenticated:

        flight = get_object_or_404(
            Flight,
            flight_iata=flight_iata.upper()
        )

        return render(
            request,
            "flights/flight_detail.html",
            {
                "flight": flight,
            }
        )

    # ----------------------------------------------------
    # Guest users retrieve the flight directly from API
    # ----------------------------------------------------

    try:

        result = search_flight(
            flight_iata.upper()
        )

        if not result.get("data"):

            return render(
                request,
                "flights/flight_detail.html",
                {
                    "flight": None,
                    "error": "No flight information was found."
                }
            )

        item = result["data"][0]

        departure = item.get("departure") or {}
        arrival = item.get("arrival") or {}
        airline = item.get("airline") or {}
        flight_data = item.get("flight") or {}
        aircraft = item.get("aircraft") or {}
        live = item.get("live") or {}

        guest_flight = {
            "flight_iata": flight_data.get("iata"),
            "flight_number": flight_data.get("number"),
            "flight_icao": flight_data.get("icao"),
            "flight_status": item.get(
                "flight_status",
                "unknown"
            ),

            "airline_name": airline.get("name"),
            "airline_iata": airline.get("iata"),
            "airline_icao": airline.get("icao"),

            "departure_iata": departure.get("iata"),
            "departure_airport": departure.get("airport"),
            "departure_timezone": departure.get("timezone"),
            "departure_terminal": departure.get("terminal"),
            "departure_gate": departure.get("gate"),
            "departure_delay": departure.get("delay"),
            "departure_scheduled": departure.get("scheduled"),
            "departure_estimated": departure.get("estimated"),
            "departure_actual": departure.get("actual"),
            "departure_estimated_runway": departure.get(
                "estimated_runway"
            ),
            "departure_actual_runway": departure.get(
                "actual_runway"
            ),

            "arrival_iata": arrival.get("iata"),
            "arrival_airport": arrival.get("airport"),
            "arrival_timezone": arrival.get("timezone"),
            "arrival_terminal": arrival.get("terminal"),
            "arrival_gate": arrival.get("gate"),
            "arrival_baggage": arrival.get("baggage"),
            "arrival_delay": arrival.get("delay"),
            "arrival_scheduled": arrival.get("scheduled"),
            "arrival_estimated": arrival.get("estimated"),
            "arrival_actual": arrival.get("actual"),
            "arrival_estimated_runway": arrival.get(
                "estimated_runway"
            ),
            "arrival_actual_runway": arrival.get(
                "actual_runway"
            ),

            "aircraft_registration": aircraft.get(
                "registration"
            ),
            "aircraft_iata": aircraft.get("iata"),
            "aircraft_icao": aircraft.get("icao"),
            "aircraft_icao24": aircraft.get("icao24"),

            "latitude": live.get("latitude"),
            "longitude": live.get("longitude"),
            "altitude": live.get("altitude"),
            "direction": live.get("direction"),
            "speed_horizontal": live.get(
                "speed_horizontal"
            ),
            "speed_vertical": live.get(
                "speed_vertical"
            ),
        }

        return render(
            request,
            "flights/flight_detail.html",
            {
                "flight": guest_flight,
            }
        )

    except Exception as e:

        return render(
            request,
            "flights/flight_detail.html",
            {
                "flight": None,
                "error": str(e)
            }
        )