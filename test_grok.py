import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROK_API_KEY")

if not api_key:
    raise ValueError("GROK_API_KEY was not found in .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Hello. Respond with: Flight Intelligence AI is working."
)

print(response.output_text)