# Flight Intelligence — FlightIQ AI

Flight Intelligence is a Django-based web application for searching, storing and analysing flight information. The application integrates the Aviationstack API for flight data and uses Groq through an OpenAI-compatible API to power the specialised **FlightIQ AI** assistant.

The system combines flight search, detailed flight information, user authentication, search history and AI-powered natural-language flight queries within a single web application.

---

## Features

### Flight Intelligence

- Professional flight information dashboard
- Flight search by IATA flight number
- Detailed flight information pages
- Aviationstack API integration
- SQLite database for stored flight records
- Flight status information
- Departure and arrival information
- Flight delays
- Departure and arrival terminals
- Gates
- Arrival baggage information
- Aircraft information
- Live aircraft information when available
- Flight data source and update timestamps

### FlightIQ AI

- Specialised flight-information AI assistant
- Natural-language flight questions
- AI intent classification
- Structured flight query processing
- Database-backed responses
- Grounded responses using verified flight information
- Protection against unrelated questions
- Specific flight queries
- Delayed flight queries
- Active flight queries
- Scheduled flight queries
- Cancelled flight queries
- Airline-based flight queries
- Departure airport queries
- Arrival airport queries

### User Accounts

- User registration
- User login
- User logout
- Authenticated user sessions
- Account/profile page
- Member information
- Personal flight search history
- Search history linked to stored flight records

### Guest Access

Users can search for flights without creating an account.

Guest users can:

- Search flights
- View flight information
- View detailed flight information
- Use FlightIQ AI where supported

Guest flight searches are not stored in personal search history.

Authenticated users receive additional persistence through their account and flight search history.

---

# Technology Stack

- Python 3.12
- Django 6.1.1
- SQLite
- Aviationstack API
- Groq API
- OpenAI Python SDK
- Requests
- python-dotenv
- HTML
- CSS
- JavaScript
- Docker
- Docker Compose
- Docker Desktop

---

# Project Structure

```text
flight-intelligence-FlightIQ-AI/
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
├── users/
│   ├── views.py
│   └── urls.py
│
├── templates/
│   ├── base.html
│   ├── dashboard/
│   ├── flights/
│   ├── chatbot/
│   └── users/
│
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── .env
├── db.sqlite3
├── test_aviationstack.py
├── test_grok.py
└── README.md