import requests
from django.conf import settings


class AviationStackClient:

    BASE_URL = "https://api.aviationstack.com/v1"

    def __init__(self):
        self.api_key = settings.AVIATIONSTACK_API_KEY

    def get_flights(self, **params):
        """
        Retrieve flight information from Aviationstack.
        """

        params["access_key"] = self.api_key

        response = requests.get(
            f"{self.BASE_URL}/flights",
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()