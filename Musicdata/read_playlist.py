import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up authentication credentials
scope = "user-library-read user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Get information about the currently playing track
current_track = sp.current_playback()

# Check if the current track is part of a playlist
if current_track['context'] is not None and 'uri' in current_track['context']:
    # Get the URI of the queue playlist
    playlist_uri = current_track['context']['uri']
    #print(playlist_uri)
    a=playlist_uri.rsplit(":") #extracting the string uri without the definitive token names
    # Get information about the tracks in the queue playlist
    playlist_items = sp.playlist_items(playlist_id=a[4], fields='items(track(name, artists(name)))')

    # Print the details of each track in the queue
    for item in playlist_items['items']:
        track = item['track']
        print(f"Track: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print()

else:
    print("There is no queue playlist currently playing.")
