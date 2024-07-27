import requests
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
        tracks = get_recommended_songs_by_genre_and_tempo(token, genre, tempo) if tempo else get_recommended_songs_by_genre_and_tempo(token, genre, 100)
        playlist = [{"name": track["name"], "artist": track["artists"][0]["name"]} for track in tracks]
        
        # Generate playlist URL logic
        playlist_url = "https://open.spotify.com/embed/playlist/" + "your_generated_playlist_id"
        
        return playlist_url
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def create_empty_playlist(user_id, playlist_name):
    try:
        token = get_token() 
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        data = {
            'name': playlist_name, # what would we set this? 
            'public': False  # adjust privacy of playlist
        }
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201: # success
            playlist_id = response.json()['id']
            return playlist_id
        else:
            print(f"Failed to create playlist: {response.status_code} - {response.text}")
            return None
        
    except Exception as e:
        print(f"Error occurred while creating playlist: {str(e)}")
        return None

def add_tracks_to_playlist(playlist_id, tracks):
    try:
        token = get_token()  
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        uris = [f'spotify:track:{track["id"]}' for track in tracks] # assume tracks have track IDs

        data = {
            'uris': uris
        }
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print("Tracks added successfully.")
            return True
        else:
            print(f"Failed to add tracks: {response.status_code} - {response.text}")
            return False
        
    except Exception as e:
        print(f"Error occurred while adding tracks: {str(e)}")
        return False
