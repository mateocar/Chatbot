import json
import random
import joblib

model = joblib.load("app/chat_model.pkl")

with open("app/intens.json", "r") as intt:
    intents = json.load(intt)

def get_response(user_input: str) -> str:
    tag = model.predict([user_input])[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
    
    return "Lo siento no entendi lo copiaste"