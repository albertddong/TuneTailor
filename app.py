from flask import Flask, request, jsonify
from app.playlist import get_playlist_for_user_input

app = Flask(__name__)

@app.route('/getPlaylist', methods=['POST'])
def get_playlist():
    data = request.json
    user_input = data.get('input')
    playlist = get_playlist_for_user_input(user_input)
    return jsonify(playlist)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
