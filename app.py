from flask import Flask, jsonify, redirect, session, request
from flask_cors import CORS
import logging
import requests
from server.playlist import get_playlist_for_user_input
from dotenv import load_dotenv
import urllib.parse
import os
from datetime import datetime

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
CORS(app)  # This will allow requests from any origin

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
AUTH_URL = 'https://accounts.spotify.com/authorize'
REDIRECT_URI = 'http://localhost:3000'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

@app.route('/test', methods=['GET'])
def test():
    app.logger.debug("test function called")
    return jsonify({'message': 'Test route is working'})

@app.route('/')
def index():
    return "Spotify App <a href='/login'>Login with Spotify</a>"

@app.route('/login')
def login():
    app.logger.debug("login function called")
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

@app.route('/getPlaylist', methods=['GET'])
def get_playlist():
    app.logger.debug("playlist function called")
    mood = request.args.get('mood')
    tempo = request.args.get('tempo')
    user_input = f"Mood: {mood}, Tempo: {tempo}"
    
    playlist_url = get_playlist_for_user_input(user_input)
    return jsonify({'url': playlist_url})

@app.route('/callback')
def callback():
    app.logger.debug("callback function called")
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

        return redirect('/test')

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

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/testing')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

