# Flight Intelligence

Flight Intelligence is a Django-based web application for searching, storing, and analysing flight information. It integrates the Aviationstack API for flight data and Groq-powered AI through an OpenAI-compatible API for the FlightIQ AI assistant.

## Features

- Professional flight information dashboard
- Flight search by IATA flight number
- Detailed flight information pages
- SQLite database for stored flight records
- Aviationstack API integration
- Flight status, departure, arrival, delay, terminal, baggage and aircraft information
- FlightIQ AI assistant powered by Groq
- Natural-language flight questions
- AI intent classification for flight-related requests
- Database-backed AI responses to reduce hallucination
- Automatic rejection of unrelated questions
- Queries for:
  - Specific flights
  - Delayed flights
  - Active flights
  - Scheduled flights
  - Cancelled flights
  - Airline flights
  - Departure airport flights
  - Arrival airport flights

## Technology Stack

- Python 3.12
- Django
- SQLite
- Aviationstack API
- Groq API
- OpenAI Python SDK
- HTML/CSS
- python-dotenv

## Project Structure

```text
flight-intelligence/
│
├── chatbot/
│   ├── flight_tools.py
│   ├── grok_client.py
│   ├── intent_parser.py
│   ├── query_dispatcher.py
│   ├── services.py
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── dashboard/
│   ├── views.py
│   └── urls.py
│
├── flights/
│   ├── models.py
│   ├── views.py
│   ├── services.py
│   ├── api_client.py
│   ├── admin.py
│   └── urls.py
│
├── templates/
│   ├── dashboard/
│   ├── flights/
│   └── chatbot/
│
├── manage.py
├── requirements.txt
├── test_aviationstack.py
├── test_grok.py
├── .env
└── .gitignore
```

## Architecture

```text
                         User
                           │
                           ▼
                    Flight Intelligence
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
       Flight Explorer              FlightIQ AI
             │                           │
             ▼                           ▼
       Aviationstack              Groq Intent Parser
             │                           │
             ▼                           ▼
           SQLite                 Query Dispatcher
                                         │
                                         ▼
                                      SQLite
                                         │
                                         ▼
                                  Verified Flight Data
                                         │
                                         ▼
                                        Groq
                                         │
                                         ▼
                                Natural-language answer
```

## Installation

### 1. Clone or copy the project

```powershell
cd D:\flight-intelligence
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

If the requirements file does not yet contain the required packages:

```powershell
pip install django requests python-dotenv openai
```

## Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

AVIATIONSTACK_API_KEY=your_aviationstack_api_key
GROK_API_KEY=your_groq_api_key
```

### Security

Never commit `.env` or API keys to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
db.sqlite3
```

If an API key is accidentally exposed, revoke it and generate a replacement.

## Database Setup

Run:

```powershell
python manage.py makemigrations
python manage.py migrate
```

Create an administrator if required:

```powershell
python manage.py createsuperuser
```

## Running the Application

Start the Django development server:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Main Pages

### Dashboard

```text
http://127.0.0.1:8000/
```

Provides:

- Total flight count
- Active flights
- Delayed flights
- Scheduled flights
- Cancelled flights
- Recently updated flights
- Flight search

### Flight Explorer

```text
http://127.0.0.1:8000/flights/
```

Search for flights such as:

```text
EK202
```

### Flight Details

Example:

```text
http://127.0.0.1:8000/flights/flight/EK202/
```

### FlightIQ AI

```text
http://127.0.0.1:8000/ai-assistant/
```

Users can enter natural-language questions without following predefined questions.

Examples:

```text
Is EK202 delayed?
```

```text
What terminal does EK202 arrive at?
```

```text
Which flights are delayed?
```

```text
Which Emirates flights are active?
```

```text
Which flights are arriving at DXB?
```

FlightIQ AI should reject unrelated requests such as:

```text
Where can I get food?
```

```text
Where can I catch the train?
```

## Aviationstack Integration

The application uses Aviationstack to obtain flight information.

The API client is located at:

```text
flights/api_client.py
```

The main endpoint used is:

```text
https://api.aviationstack.com/v1/flights
```

A typical request searches using a flight IATA code:

```python
client.get_flights(
    flight_iata="EK202"
)
```

The returned data is transformed and stored in the Django `Flight` model.

## Flight Data Model

The `Flight` model stores information including:

- Flight date
- Flight status
- Flight number
- IATA and ICAO identifiers
- Airline information
- Departure airport
- Departure terminal and gate
- Departure delay
- Scheduled, estimated and actual departure times
- Arrival airport
- Arrival terminal and gate
- Arrival baggage
- Arrival delay
- Scheduled, estimated and actual arrival times
- Aircraft information
- Live latitude and longitude when available
- Altitude
- Direction
- Horizontal and vertical speed
- Data source
- Last database update

Live fields are nullable because the Aviationstack response may not contain live position data.

## FlightIQ AI

FlightIQ AI is designed as a specialised flight-information assistant rather than a general-purpose chatbot.

### Intent Detection

The intent parser identifies whether a user request is flight-related.

Supported intents include:

```text
flight_details
delayed_flights
active_flights
scheduled_flights
cancelled_flights
airline_flights
departure_flights
arrival_flights
unknown
```

It also extracts relevant criteria such as:

- Flight IATA code
- Airline name
- Airport IATA code
- Airport name

### Database Query Layer

The query dispatcher converts the structured intent into a Django database operation.

This prevents the AI model from directly inventing flight information.

For example:

```text
User:
Is EK202 delayed?

        ↓

Groq:
flight_details
EK202

        ↓

Django:
Find EK202 in SQLite

        ↓

SQLite:
Arrival delay = 15 minutes

        ↓

Groq:
Generate answer from verified data

        ↓

FlightIQ AI:
EK202 has an arrival delay of 15 minutes.
```

## AI Safety and Grounding

FlightIQ AI follows these principles:

1. Flight data comes from the application database.
2. Groq does not directly control the database.
3. The AI should not invent missing flight information.
4. Missing values should be reported as unavailable.
5. Non-flight questions should receive a polite refusal.
6. Database results should be used as the source of truth.
7. The application should distinguish stored data from genuinely live information.

## Testing

### Test Aviationstack

Run:

```powershell
python test_aviationstack.py
```

A successful request should return HTTP 200 and flight data.

### Test Groq

Run:

```powershell
python test_grok.py
```

Expected output:

```text
Flight Intelligence AI is working.
```

### Test Django Groq Integration

Run:

```powershell
python manage.py shell
```

Then:

```python
from chatbot.grok_client import GrokClient

client = GrokClient()

response = client.ask(
    "Say exactly: Django Flight Intelligence is connected to Groq."
)

print(response)
```

Expected:

```text
Django Flight Intelligence is connected to Groq.
```

### Test Flight Tools

```python
from chatbot.flight_tools import get_flight, format_flight

flight = get_flight("EK202")

print(flight)
print(format_flight(flight))
```

### Test Intent Parser

```python
from chatbot.intent_parser import FlightIntentParser

parser = FlightIntentParser()

print(parser.parse("Is EK202 delayed?"))
print(parser.parse("Which flights are delayed?"))
print(parser.parse("Which Emirates flights are active?"))
print(parser.parse("Which flights are arriving at DXB?"))
print(parser.parse("Where can I get food?"))
```

### Test Query Dispatcher

```python
from chatbot.intent_parser import FlightIntentParser
from chatbot.query_dispatcher import dispatch_flight_query

parser = FlightIntentParser()

intent = parser.parse("Is EK202 delayed?")
result = dispatch_flight_query(intent)

print(result)
```

## Current Example Data

The current development database contains a tested Emirates flight:

```text
Flight: EK202
Airline: Emirates
Departure: JFK
Arrival: DXB
Status: Active
Departure Terminal: 4
Arrival Terminal: 3
Arrival Delay: 15 minutes
```

This is development/test data and should not be treated as permanently current flight information.

## API Quota and Data Freshness

Aviationstack usage should be minimised because API plans impose request limits.

The application therefore follows a database-first approach:

```text
User search
    ↓
Check SQLite
    ↓
If available → use stored record
    ↓
If unavailable → request Aviationstack
    ↓
Store returned flight
```

A future production version should add a configurable data-refresh/freshness mechanism so that stale flight records can be refreshed without unnecessarily consuming API requests.

## Future Improvements

Planned improvements include:

- Proper multi-turn conversation history
- Chat-style messaging interface
- Dynamic flight-data refresh
- Flight/date-aware database uniqueness
- More advanced natural-language queries
- Combined filters such as airline + status + airport
- Flight tracking visualisation
- Better Markdown rendering
- Loading indicators
- Error handling for API limits
- User authentication
- Saved conversations
- Production deployment
- Automated tests
- Logging and monitoring

## Development Notes

The application deliberately separates:

```text
AI interpretation
```

from:

```text
Database operations
```

This architecture makes the system easier to maintain and reduces the risk of hallucinated flight information.

The preferred flow is:

```text
Natural-language question
        ↓
Intent classification
        ↓
Structured request
        ↓
Django query
        ↓
Verified data
        ↓
AI response generation
```

## License

This project is currently a development/academic project. Add an appropriate open-source or proprietary license before public distribution.
