from flights.models import Flight

from .context_builder import build_flight_context
from .grok_client import GrokClient


def answer_flight_question(flight_iata, user_question):

    flight = Flight.objects.filter(
        flight_iata__iexact=flight_iata
    ).first()

    if not flight:
        return (
            f"I could not find flight {flight_iata} "
            "in the Flight Intelligence database."
        )

    flight_context = build_flight_context(flight)

    prompt = f"""
You are the AI assistant for Flight Intelligence.

Answer the user's question using ONLY the supplied
flight data.

IMPORTANT RULES:

1. Never invent flight information.
2. Never assume a missing value.
3. If a value is None or unavailable, clearly state
   that the information is not available.
4. Do not create a flight status that is not present
   in the supplied data.
5. Keep answers concise and professional.
6. When relevant, mention the flight number and
   airport IATA codes.
7. Distinguish between scheduled, estimated and actual
   times.
8. If the user asks about delay, use the supplied
   delay values.
9. If live position information is unavailable,
   explicitly say that live position data is unavailable.

FLIGHT DATA:

{flight_context}

USER QUESTION:

{user_question}
"""

    client = GrokClient()

    return client.ask(prompt)