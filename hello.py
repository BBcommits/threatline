import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="In two sentences, explain what prompt injection is.",
)

print(response.text)