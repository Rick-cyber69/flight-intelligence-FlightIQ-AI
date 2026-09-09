import json

from django.conf import settings
from openai import OpenAI


class FlightIntentParser:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.GROK_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )

    def parse(self, question):

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are the intent classifier for FlightIQ AI.

FlightIQ AI is a specialised flight-information assistant.

Determine whether the user's question is related to:
- flights
- airlines
- airports
- flight schedules
- flight status
- delays
- departures
- arrivals
- terminals
- gates
- aircraft
- flight routes

If the question is NOT related to these topics,
set is_flight_related to false.

Never answer the user's question.

Only classify the request and extract relevant
search information.

Available intents:

flight_details
delayed_flights
active_flights
scheduled_flights
cancelled_flights
airline_flights
departure_flights
arrival_flights
unknown

Use flight_details when the user asks about a
specific flight.

Use delayed_flights when the user asks about
delayed flights generally.

Use active_flights when the user asks about
currently active flights.

Use scheduled_flights when the user asks about
scheduled flights.

Use cancelled_flights when the user asks about
cancelled flights.

Use airline_flights when the user asks about
flights belonging to a particular airline.

Use departure_flights when the user asks about
flights departing from a particular airport.

Use arrival_flights when the user asks about
flights arriving at a particular airport.

Extract:
- flight IATA code such as EK202
- airline name such as Emirates
- airport IATA code such as DXB or JFK
- airport name when mentioned

If something is not available, use null.
""",
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "flight_intent",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "is_flight_related": {
                                "type": "boolean"
                            },
                            "intent": {
                                "type": "string",
                                "enum": [
                                    "flight_details",
                                    "delayed_flights",
                                    "active_flights",
                                    "scheduled_flights",
                                    "cancelled_flights",
                                    "airline_flights",
                                    "departure_flights",
                                    "arrival_flights",
                                    "unknown"
                                ]
                            },
                            "flight_iata": {
                                "type": ["string", "null"]
                            },
                            "airline_name": {
                                "type": ["string", "null"]
                            },
                            "airport_iata": {
                                "type": ["string", "null"]
                            },
                            "airport_name": {
                                "type": ["string", "null"]
                            }
                        },
                        "required": [
                            "is_flight_related",
                            "intent",
                            "flight_iata",
                            "airline_name",
                            "airport_iata",
                            "airport_name"
                        ],
                        "additionalProperties": False
                    }
                }
            }
        )

        content = response.choices[0].message.content

        return json.loads(content)