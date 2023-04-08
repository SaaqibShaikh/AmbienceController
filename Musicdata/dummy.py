# # # shows audio analysis for the given track
# # # print("ui")
# # # from __future__ import print_function    # (at top of module)
# # from spotipy.oauth2 import SpotifyClientCredentials
# # import json
# # import spotipy
# # import time
# # import sys
# # client_credentials_manager = SpotifyClientCredentials()
# # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# # print(sys.argv)
# # if len(sys.argv) > 1:
# #     tid = sys.argv[1]
# # else:
# #     print("There is no queue playlist currently playing.")
# #     # tid = 'spotify:track:2mj1Z5bqu0UfW4o4a7UxpW'
# #
# #
# # def fetch_analysis(track):
# #     start = time.time()
# #     analysis = sp.audio_analysis(track)
# #     delta = time.time() - start
# #     print(json.dumps(analysis, indent=4))
# #     print("analysis retrieved in %.2f seconds" % (delta,))
# #
# #
# # def fetch_features(track):
# #     start = time.time()
# #     features = sp.audio_features(track)
# #     delta = time.time() - start
# #     print(json.dumps(features, indent=4))
# #     print("analysis retrieved in %.2f seconds" % (delta,))
# #     print(features)
# #     return features
# # fetch_analysis('2mj1Z5bqu0UfW4o4a7UxpW')
#
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import time
#
#
#
# while True:
#     try:
#         # Set up authentication credentials
#         scope = "user-read-playback-state"
#         sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#
#         # Get information about the currently playing track
#         current_track = sp.current_playback()
#         # print(type(current_track))
#         print(current_track)
#         # Get the name of the track, artist, and album
#         track_name = current_track['item']['name']
#         artist_name = current_track['item']['artists'][0]['name']
#         album_name = current_track['item']['album']['name']
#
#         # Get the current playback position in seconds
#         position_ms = current_track['progress_ms']
#         position_sec = int(position_ms / 1000)
#
#         # Print the details of the current track
#         print(f"Track: {track_name}")
#         print(f"Artist: {artist_name}")
#         print(f"Album: {album_name}")
#         print(f"Position: {position_sec} seconds")
#         # print(current_track)
#         # print({})
#         time.sleep(0.5)
#     except TypeError:
#         print("Status_default")
#
# fetchplayback()
#
# shows audio analysis for the given track
# print("ui")
# from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
print(sys.argv)
if len(sys.argv) > 1:
    tid = sys.argv[1]
else:
    print("There is no queue playlist currently playing.")
    # tid = 'spotify:track:2mj1Z5bqu0UfW4o4a7UxpW'


def fetch_analysis(track):
    start = time.time()
    analysis = sp.audio_analysis(track)
    delta = time.time() - start
    print(json.dumps(analysis, indent=4))
    print("analysis retrieved in %.2f seconds" % (delta,))


def fetch_features(track):
    start = time.time()
    features = sp.audio_features(track)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    #print("analysis retrieved in %.2f seconds" % (delta,))
    #print(features)
    return features
fetch_analysis('2mj1Z5bqu0UfW4o4a7UxpW')

