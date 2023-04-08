# Shows a user's saved tracks (need to be authenticated via oauth)
import time

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import fetch_playback as f
import track_analysis as t
def get_currentposition():
    time = int(result['progress_ms'] / 1000)
    return time


def get_tracktime():
    total_time = int(result['item']['duration_ms']/1000)
    #print(total_time)
    return total_time

try:
    while True:
        scope = 'user-read-playback-state'
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='', client_secret='', scope=scope, redirect_uri=''))
        result = sp.current_playback()
        print(result)
        track_uri = result['item']['external_urls']['spotify']
        track_name = result['item']['name']
        track_sus = result['item']
        track_properties = sp.track(track_uri)
        print("Printing Track properties",track_properties)
        print("Track popularity on a scale of 0 to 1: ",track_properties['popularity'])
        # print(track_sus)


        # # test_1 = sp.artist(track_sus["artists"][0]["external_urls"]["spotify"])
        # # test_1 = sp.track(track_uri)
        # # track_uri = 'spotify:track:2mj1Z5bqu0UfW4o4a7UxpW'
        # print(test_1)

        # print("artist genres:", test_1["genres"])
        print("Track name is: ",track_name)
        currenttrack_features = t.fetch_features(track_uri)
        currenttrack_tempo = currenttrack_features[0]['tempo']
        currenttrack_valence = currenttrack_features[0]['valence']
        currenttrack_acousticness = currenttrack_features[0]['acousticness']
        currenttrack_speechiness = currenttrack_features[0]['speechiness']
        cur_pos = get_currentposition()
        track_length = get_tracktime()
        relative_pos = track_length-cur_pos
        if (relative_pos >= 3 and cur_pos >= 2):
            if (currenttrack_tempo>=140):
                print("red")
            elif (currenttrack_valence>=0.5):
                print("Yellow")
            #     if(currenttrack_acousticness>=0.6):
            #         print("Positive Acoustic")
            #         continue
            #     if(currenttrack_speechiness>=0.6):
            #         print("Not acoustic but speechy, basically COUNTRY")
            #         continue
            #     if(currenttrack_tempo<80):
            #         print("something")
            #     elif(currenttrack_tempo>=80 and currenttrack_tempo<= 100):
            #         print("something 2.0")
            #     elif(currenttrack_tempo>=100 and currenttrack_tempo<= 130):
            #         print("something 3.0")
            #     elif(currenttrack_tempo>=130 and currenttrack_tempo<= 160):
            #         print("something 4.0")
            #     elif(currenttrack_tempo>=160 and currenttrack_tempo<=220):
            #         print("something 3.0")
            #     elif(currenttrack_tempo>=220):
            #         print("Flickering red killer rock music")
            else:
                print("green")
        else:
            print("default white light maybe or red")
        time.sleep(3)
except TimeoutError:
    print()
    print()
    print("sus")
    time.sleep(2)


# while True:
#      t.fetch_analysis(track_uri)
def fetch_playingstatus():
    print("ho")

"""if result is not None:
    a = dict(result['device'])
    print(a['is_active'])"""