from django.shortcuts import render, get_object_or_404

from .models import Flight
from .services import search_flight, save_flight


def flight_search(request):

    flight_number = request.GET.get(
        "flight",
        ""
    ).strip().upper()

    flights = Flight.objects.all()

    searched = False
    error = None

    if flight_number:

        searched = True

        # Search database first
        flights = flights.filter(
            flight_iata__icontains=flight_number
        )

        # If database has no result,
        # try Aviationstack
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