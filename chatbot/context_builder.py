def build_flight_context(flight):
    return f"""
FLIGHT INFORMATION

Flight:
{flight.flight_iata}

Flight Number:
{flight.flight_number}

Flight ICAO:
{flight.flight_icao}

Flight Date:
{flight.flight_date}

Status:
{flight.flight_status}

Airline:
{flight.airline_name}

Airline IATA:
{flight.airline_iata}

Airline ICAO:
{flight.airline_icao}

DEPARTURE

Airport:
{flight.departure_airport}

IATA:
{flight.departure_iata}

ICAO:
{flight.departure_icao}

Terminal:
{flight.departure_terminal}

Gate:
{flight.departure_gate}

Delay:
{flight.departure_delay}

Scheduled:
{flight.departure_scheduled}

Estimated:
{flight.departure_estimated}

Actual:
{flight.departure_actual}

ARRIVAL

Airport:
{flight.arrival_airport}

IATA:
{flight.arrival_iata}

ICAO:
{flight.arrival_icao}

Terminal:
{flight.arrival_terminal}

Gate:
{flight.arrival_gate}

Baggage:
{flight.arrival_baggage}

Delay:
{flight.arrival_delay}

Scheduled:
{flight.arrival_scheduled}

Estimated:
{flight.arrival_estimated}

Actual:
{flight.arrival_actual}

AIRCRAFT

Registration:
{flight.aircraft_registration}

IATA:
{flight.aircraft_iata}

ICAO:
{flight.aircraft_icao}

ICAO24:
{flight.aircraft_icao24}

LIVE POSITION

Latitude:
{flight.latitude}

Longitude:
{flight.longitude}

Altitude:
{flight.altitude}

Direction:
{flight.direction}

Horizontal Speed:
{flight.speed_horizontal}

Vertical Speed:
{flight.speed_vertical}

DATABASE

Last Updated:
{flight.last_updated}

Data Source:
{flight.data_source}
"""