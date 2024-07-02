from .spotify import get_token, get_genre_seeds, get_recommended_songs_by_genre
from .nlp import parse_user_input

def get_playlist_for_user_input(input_text):
    intent = parse_user_input(input_text)
    genre = ''

    if intent == 'happy':
        genre = 'happy'
    elif intent == 'sad':
        genre = 'sad'
    else:
        genre = 'pop'

    token = get_token()
    all_genres = get_genre_seeds(token)
    if genre in all_genres:
        songs = get_recommended_songs_by_genre(token, genre)
    else:
        songs = get_recommended_songs_by_genre(token, 'pop')
    
    return songs
