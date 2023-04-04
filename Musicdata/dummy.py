# # shows audio analysis for the given track
# print("ui")
# #from __future__ import print_function    # (at top of module)
# from spotipy.oauth2 import SpotifyClientCredentials
# import json
# import spotipy
# import time
# import sys
# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# #print(sys.argv)
# if len(sys.argv) > 1:
#     tid = sys.argv[1]
# else:
#     print("There is no queue playlist currently playing.")
#     tid = 'spotify:track:2mj1Z5bqu0UfW4o4a7UxpW'
# start = time.time()
# analysis = sp.audio_analysis('4rAg5bbrdZX00mXXhLvYXj')
# delta = time.time() - start
# print(sys.platform)
# print(json.dumps(analysis, indent=4))
# print("analysis retrieved in %.2f seconds" % (delta,))
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
    print(analysis.keys())
    print(json.dumps(analysis['sections'], indent=4))
    print("analysis retrieved in %.2f seconds" % (delta,))



def fetch_features(track):
    start = time.time()
    features = sp.audio_features(track)
    delta = time.time() - start
    print(json.dumps(features, indent=4))
    print("analysis retrieved in %.2f seconds" % (delta,))

fetch_analysis('2mj1Z5bqu0UfW4o4a7UxpW')