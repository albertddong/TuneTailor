from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

# loads the environment variable file 
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    # make the post request from the request package w/ necessary info
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    # q = {__insert what you are querying__}&type=___insert what you want____
    # this is essentially combining all the search parameters 
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_genre_seeds(token):
    headers = get_auth_header(token)
    result = get("https://api.spotify.com/v1/recommendations/available-genre-seeds", headers=headers)
    json_result = json.loads(result.content)["genres"]
    return json_result

token = get_token()
all_genres = get_genre_seeds(token)

def get_recommended_songs_by_genre(token, genre):
    if genre in all_genres:
        url = "https://api.spotify.com/v1/recommendations"
        headers = get_auth_header(token)
        query = f"?limit=5&seed_genres={genre}"

        query_url = url + query 
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)
        return json_result.get("tracks", [])
    else:
        print("Unsupported genre...")
        return None


# # this is just for testing
# tracks = get_recommended_songs_by_genre(token, "classical")
# for track in tracks:
#     print(track["name"])