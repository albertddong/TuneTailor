from .spotify import get_token, get_recommended_songs_by_genre_and_tempo
from .nlp import detect_mood, detect_tempo

def get_playlist_for_user_input(input_text):
    try:
        user_input = input_text

        mood = detect_mood(user_input)
        tempo = detect_tempo(user_input)
        print(f"Detected Mood: {mood}")  
        print(f"Detected Tempo: {tempo}")  
        genre = "pop"  

        if mood:
            if mood == "happy":
                genre = "pop"
            elif mood == "sad":
                genre = "blues"
        
        token = get_token()
        tracks = get_recommended_songs_by_genre_and_tempo(token, genre, tempo) if tempo else []

        playlist = [{"name": track["name"], "artist": track["artists"][0]["name"]} for track in tracks]
        return playlist
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return [] 
