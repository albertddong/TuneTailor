from urllib.parse import urlencode
from flask import Flask, jsonify, redirect, session, request, url_for
from flask_cors import CORS
import logging
import os
from datetime import datetime
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
from dotenv import load_dotenv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.logger.setLevel(logging.DEBUG)

# Allow requests from http://localhost:3000 with credentials
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "supports_credentials": True
    }
})
# Load environment variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:5000/callback'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
scope = 'user-read-private,user-read-email,playlist-read-private,playlist-modify-private,playlist-modify-public'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=REDIRECT_URI,
    scope=scope,
    cache_handler=cache_handler,
    show_dialog=True
)

@app.route('/')
def index():
    app.logger.debug("index function called")
    token_info = cache_handler.get_cached_token()
    if not token_info or not sp_oauth.validate_token(token_info):
        auth_url = sp_oauth.get_authorize_url()
        app.logger.debug(f"Sending Spotify auth URL to client: {auth_url}")
        return jsonify({"auth_url": auth_url})
    app.logger.debug("User is authenticated, redirecting to website")
    return jsonify({"status": "authenticated"})

@app.route('/callback')
def callback():
    app.logger.debug("callback function called")
    access_token = ""
    try:
        auth_code = request.args['code']
        token_info = sp_oauth.get_access_token(auth_code)
        app.logger.debug(f"Access token obtained: {token_info}")
        cache_handler.save_token_to_cache(token_info)
        access_token = token_info['access_token']
        app.logger.debug(access_token)
    except Exception as e:
        app.logger.error(f"Error obtaining access token: {e}")
        return jsonify({"error": "Failed to obtain access token"}), 500
    
    try:
        # Properly encode the access token in the URL
        frontend_redirect_url = f"http://localhost:3000?{urlencode({'access_token': access_token})}"
        app.logger.debug(f"Redirecting to frontend with URL: {frontend_redirect_url}")
        return redirect(frontend_redirect_url)
    except Exception as e:
        app.logger.error(f"Error during redirect: {e}")
        return jsonify({"error": "Failed to redirect to frontend"}), 500

# def callback():
#     app.logger.debug("callback function called")
#     auth_code = request.args.get('code')
#     if not auth_code:
#         app.logger.error("Authorization code is missing in the request")
#         return jsonify({"error": "Authorization code is missing"}), 400
    
#     app.logger.debug(f"Authorization code received: {auth_code}")
#     try:
#         token_info = sp_oauth.get_access_token(auth_code)
#         app.logger.debug(f"Access token obtained: {token_info}")
#         cache_handler.save_token_to_cache(token_info)
#         access_token = token_info['access_token']
#     except Exception as e:
#         app.logger.error(f"Error obtaining access token: {e}")
#         return jsonify({"error": "Failed to obtain access token"}), 500

#     # Redirect back to the frontend with the access token as a query parameter
#     frontend_redirect_url = f"http://localhost:3000?access_token={access_token}"
#     return redirect(frontend_redirect_url)

# @app.route('/get_playlists')
# def get_playlists():
#     app.logger.debug("get_playlists function called")
#     token_info = cache_handler.get_cached_token()
#     if not token_info or not sp_oauth.validate_token(token_info):
#         app.logger.debug("User is not authenticated, redirecting to Spotify auth URL")
#         auth_url = sp_oauth.get_authorize_url()
#         app.logger.debug(auth_url)
#         return redirect(auth_url)
    
#     sp = Spotify(auth=token_info['access_token'])
#     playlists = sp.current_user_playlists()
#     playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
#     playlists_html = '<br>'.join([f'{name}: {url}' for name, url in playlists_info])
    
#     app.logger.debug(f"Retrieved playlists: {playlists_info}")
#     return playlists_html
@app.route('/get_playlists')
def get_playlists():
    app.logger.debug("get_playlists function called")
    
    access_token = request.headers.get('Authorization').split(" ")[1]
    if not access_token:
        app.logger.debug("Access token not provided")
        return jsonify({"error": "Access token is required"}), 400
    
    sp = Spotify(auth=access_token)
    try:
        playlists = sp.current_user_playlists()
        playlists_info = [(pl['name'], pl['external_urls']['spotify']) for pl in playlists['items']]
        app.logger.debug(f"Retrieved playlists: {playlists_info}")
        app.logger.debug(playlists_info[0][1])
        return jsonify({"playlists": playlists_info})
    except Exception as e:
        app.logger.error(f"Error fetching playlists: {str(e)}")
        return jsonify({"error": "Failed to fetch playlists"}), 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

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

        return redirect('/testGetUserPlaylists')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
