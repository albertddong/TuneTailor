from transformers import pipeline

classifier = pipeline('sentiment-analysis')

def detect_mood(input_text):
    result = classifier(input_text)
    sentiment = result[0]['label']
    if sentiment == 'POSITIVE':
        return 'happy'
    elif sentiment == 'NEGATIVE':
        return 'sad'
    else:
        return 'neutral'

def detect_tempo(input_text):
    words = input_text.split()
    tempo_words = {
        "slow": 60,
        "relaxing": 70,
        "medium": 100,
        "fast": 120,
        "upbeat": 140
    }
    for word in words:
        if word.lower() in tempo_words:
            return tempo_words[word.lower()]
    return None
