import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class TripAdvisor():
    def __init__(self, model="gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model
        self.messages = [{"role" : "system", "content" : """
        You are a professional, friendly AI Travel Advisor. Your goal is to help the user plan a highly personalized trip.
exit
        Before you generate any travel plan, you must gather the following key information:
        1. Destination and trip duration
        2. Interests (e.g., food, museums, hiking, beaches, nightlife, shopping, etc.)
        3. Any relevant preferences or constraints (optional)

        Rules for your behavior:
        - Be welcoming and polite.
        - Ask friendly, concise follow-up questions.
        - Ask only one (or maximum two) questions at a time to not overwhelm the user.
        - Do NOT generate the final itinerary until you have gathered at least the destination, duration, and interests.
        - If the user provides contradictory or ambiguous information, politely ask for clarification before planning.

        Once you have collected all the necessary information, stop asking questions and generate a realistic, personalized travel plan using markdown formatting with exactly these sections:
        - **Trip Title**
        - **Trip Summary**
        - **Day-by-Day Itinerary**
        - **Practical Travel Tips**
        - **Estimated Budget**
        """}]
    
    def response(self, user_message):
        self.messages.append({"role" : "user", "content" : user_message})
        api_response = self.client.chat.completions.create(
        model=self.model,
        messages=self.messages)
        bot_message = api_response.choices[0].message.content
        self.messages.append({"role" : "assistant", "content" : bot_message})
        #track token usage
        input_token_usage_cost = api_response.usage.prompt_tokens*0.00000015
        output_token_usage_cost = api_response.usage.completion_tokens*0.00000060
        total_cost = input_token_usage_cost + output_token_usage_cost
        return bot_message, f'${total_cost:.6f}'

#Preis pro Input-Token: $0.00000015

#Preis pro Output-Token: $0.00000060