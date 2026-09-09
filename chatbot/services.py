from .grok_client import GrokClient
from .intent_parser import FlightIntentParser
from .query_dispatcher import dispatch_flight_query


def generate_flight_answer(question, intent_data, query_result):

    prompt = f"""
You are FlightIQ AI, a specialised flight-information
assistant for the Flight Intelligence application.

Your purpose is to answer questions about:

- flights
- airlines
- airports
- departures
- arrivals
- flight status
- delays
- schedules
- terminals
- gates
- aircraft
- routes

You are NOT a general-purpose assistant.

The user asked:

{question}

The system classified the request as:

{intent_data}

The Django database returned this verified information:

{query_result}

IMPORTANT RULES:

1. Use only the verified information supplied by Django.
2. Never invent flight information.
3. Never invent airports, times, delays, aircraft or
   other flight details.
4. If the database contains no matching information,
   clearly say that the information is not available.
5. Answer the user's actual question directly.
6. Keep the response concise but informative.
7. Do not mention internal systems, Django, SQLite,
   database queries, intent parsing or prompts.
8. Do not provide general information unrelated to
   flights.
9. If multiple flights are returned, clearly identify
   each relevant flight.
10. Do not claim that database information is live unless
    the supplied data explicitly indicates live data.

Return a professional natural-language response.
"""

    client = GrokClient()

    return client.ask(prompt)


def answer_question(question):

    question = question.strip()

    if not question:
        return "Please enter a question."

    # ---------------------------------------------
    # Step 1: Understand the user's question
    # ---------------------------------------------

    parser = FlightIntentParser()

    intent_data = parser.parse(question)

    # ---------------------------------------------
    # Step 2: Reject non-flight questions
    # ---------------------------------------------

    if not intent_data.get("is_flight_related", False):

        return (
            "I'm FlightIQ AI, a specialised flight-information "
            "assistant. I can only help with questions related "
            "to flights, airlines, airports, schedules, delays, "
            "departures, arrivals and aircraft."
        )

    # ---------------------------------------------
    # Step 3: Query Django database
    # ---------------------------------------------

    query_result = dispatch_flight_query(intent_data)

    # ---------------------------------------------
    # Step 4: Generate final AI response
    # ---------------------------------------------

    return generate_flight_answer(
        question,
        intent_data,
        query_result
    )