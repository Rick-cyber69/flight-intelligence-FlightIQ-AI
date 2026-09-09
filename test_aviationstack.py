import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("AVIATIONSTACK_API_KEY")

url = "https://api.aviationstack.com/v1/flights"

params = {
    "access_key": api_key,
    "flight_iata": "EK202",
}

response = requests.get(
    url,
    params=params,
    timeout=30
)

print(response.status_code)
print(response.json())