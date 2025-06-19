from transformers import pipeline

emotion_classifier = pipeline("text-classification", model="monologg/bert-base-cased-goemotions-original")

def detect_emotion(text):
    result = emotion_classifier(text)
    label = result[0]['label']
    score = result[0]['score']
    return label, score
