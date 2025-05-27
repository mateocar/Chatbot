import json
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

with open("app/intens.json", "r") as intt:
    data = json.load(intt)

text = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        text.append(pattern)
        labels.append(intent["tag"])

pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

pipeline.fit(text, labels)

joblib.dump(pipeline, "app/chat_model.pkl")
print("Modelo entrenado y guardado con EXITO")