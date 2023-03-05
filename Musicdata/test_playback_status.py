# Shows a user's saved tracks (need to be authenticated via oauth)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
while True:
    scope = 'user-read-playback-state'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='', client_secret='', scope=scope, redirect_uri=''))
    result = sp.current_playback()
    print(result)
    """if result is not None:
        a = dict(result['device']) 
        print(a['is_active'])"""