from django.conf import settings
from openai import OpenAI


class GrokClient:

    def __init__(self):
        self.client = OpenAI(
            api_key=settings.GROK_API_KEY,
            base_url="https://api.groq.com/openai/v1",
        )

    def ask(self, prompt):
        response = self.client.responses.create(
            model="openai/gpt-oss-20b",
            input=prompt,
        )

        return response.output_text