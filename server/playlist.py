import requests
from .spotify import get_token, get_recommended_songs_by_genre_and_tempo
from .nlp import detect_mood, detect_tempo

def get_user_id(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get('https://api.spotify.com/v1/me', headers=headers)
    if response.status_code == 200:
        return response.json()['id']
    else:
        raise Exception(f"Failed to get user ID: {response.status_code} - {response.text}")

def get_playlist_for_user_input(input_text, access_token):
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
        
        tracks = get_recommended_songs_by_genre_and_tempo(access_token, genre, tempo) if tempo else get_recommended_songs_by_genre_and_tempo(access_token, genre, 100)
        playlist = [{"name": track["name"], "artist": track["artists"][0]["name"], "id": track["id"]} for track in tracks]
        
        user_id = get_user_id(access_token)
        id = create_empty_playlist(user_id, "New Playlist", access_token)
        if not id:
            raise Exception("Failed to create playlist")
        
        playlist_url = "https://open.spotify.com/embed/playlist/" + id
        add_tracks_to_playlist(id, playlist, access_token)
        return playlist_url
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def create_empty_playlist(user_id, playlist_name, access_token):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'name': playlist_name,
            'public': False
        }
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists'
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            playlist_id = response.json()['id']
            return playlist_id
        else:
            print(f"Failed to create playlist: {response.status_code} - {response.text}")
            return None
        
    except Exception as e:
        print(f"Error occurred while creating playlist: {str(e)}")
        return None

def add_tracks_to_playlist(playlist_id, tracks, access_token):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        uris = [f'spotify:track:{track["id"]}' for track in tracks]

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
