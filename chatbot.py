import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class TripAdvisor():
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model
        self.messages = []

    def response(self):
        self.client.chat.completions.create(
        model=self.model,
        messages=self.messages)
