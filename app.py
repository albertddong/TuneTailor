from datetime import datetime
import logging
from flask import Flask, request, jsonify, redirect, session
import requests
from app.playlist import get_playlist_for_user_input
from dotenv import load_dotenv
import urllib.parse
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
REDIRECT_URI = 'http://localhost:3000'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/getPlaylist', methods=['POST'])
def get_playlist():
    data = request.json
    user_input = data.get('input')
    playlist = get_playlist_for_user_input(user_input)
    return jsonify(playlist)

@app.route('/')
def index():
    return "Spotify App <a href='/login'>Login with Spotify</a>"

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email playlist-modify-private playlist-modify-public'

    params = {
        'client_id': client_id,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)

@app.route('/callback')
def callback():
    logging.debug("callback function called")
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})

    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': client_id,
            'client_secret': client_secret
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return redirect('/playlists')

# @app.route('/playlists')
# def get_playlists():
#     if 'access_token' not in session:
#         return redirect('/login')
    
#     if datetime.now().timestamp() > session['expires_at']:
#         return redirect('/refresh-token')
    
#     headers = {
#         'Authorization': f"Bearer {session['access_token']}"
#     }

#     response = requests.get(API_BASE_URL + 'me/playlists', headers=headers)
#     playlists = response.json()

#     return jsonify(playlists)

@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': client_id,
            'client_secret': client_secret
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['acces_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/playlists')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
