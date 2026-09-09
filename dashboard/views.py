from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from flights.models import Flight


@login_required
def dashboard(request):

    total_flights = Flight.objects.count()

    active_flights = Flight.objects.filter(
        flight_status="active"
    ).count()

    delayed_flights = Flight.objects.filter(
        arrival_delay__gt=0
    ).count()

    scheduled_flights = Flight.objects.filter(
        flight_status="scheduled"
    ).count()

    cancelled_flights = Flight.objects.filter(
        flight_status="cancelled"
    ).count()

    recent_flights = Flight.objects.order_by(
        "-last_updated"
    )[:10]

    context = {
        "total_flights": total_flights,
        "active_flights": active_flights,
        "delayed_flights": delayed_flights,
        "scheduled_flights": scheduled_flights,
        "cancelled_flights": cancelled_flights,
        "recent_flights": recent_flights,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )