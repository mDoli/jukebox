import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=config.CLIENT_ID,
                                               client_secret=config.CLIENT_SECRET,
                                               redirect_uri="http://localhost:8080",
                                               scope="user-read-playback-state,user-modify-playback-state"))

devices = sp.devices()

print("Available devices:")
for device in devices["devices"]:
    print(f"Name: {device['name']}, ID: {device['id']}, Type: {device['type']}")

