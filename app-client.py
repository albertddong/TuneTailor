import requests

def get_playlist(user_input):
    url = 'http://127.0.0.1:5000/getPlaylist'
    headers = {'Content-Type': 'application/json'}
    data = {'input': user_input}
    
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        playlist = response.json()
        return playlist
    else:
        return f"Error: {response.status_code}, {response}"

if __name__ == "__main__":
    user_input = input("Enter your text: ")
    playlist = get_playlist(user_input)
    print("Playlist:", playlist)