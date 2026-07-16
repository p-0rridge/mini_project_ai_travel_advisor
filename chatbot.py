import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class TripAdvisor():
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model
        self.messages = []
        #self.messages = [{"role" : "user", "content" : "Say 'Tschüß' in Italian"}]
    
    def response(self, user_message):
        self.messages.append({"role" : "user", "content" : user_message})
        api_response = self.client.chat.completions.create(
        model=self.model,
        messages=self.messages)
        bot_message = api_response.choices[0].message.content
        self.messages.append({"role" : "assistant", "content" : bot_message})
        return bot_message
