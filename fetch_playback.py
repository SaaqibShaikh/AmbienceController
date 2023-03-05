import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication credentials
scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get information about the currently playing track
current_track = sp.current_playback()
print(type(current_track))
print(list(current_track))
# Get the name of the track, artist, and album
track_name = current_track['item']['name']
artist_name = current_track['item']['artists'][0]['name']
album_name = current_track['item']['album']['name']

# Get the current playback position in seconds
position_ms = current_track['progress_ms']
position_sec = int(position_ms / 1000)

# Print the details of the current track
print(f"Track: {track_name}")
print(f"Artist: {artist_name}")
print(f"Album: {album_name}")
print(f"Position: {position_sec} seconds")
