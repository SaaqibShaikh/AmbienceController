import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cred
cid = cred.client_ID
secret = cred.client_SECRET
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)
artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,500,50):
    track_results = sp.search(q='year:2010', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        track_name.append(t['name'])
        artist_name.append(t['artists'][0]['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
print('oldie i\'m fast as fuck')

import pandas as pd
track_dataframe = pd.DataFrame({ 'track_name' : track_name,'artist_name' : artist_name, 'track_id' : track_id, 'popularity' : popularity})
#print(track_dataframe.shape)
print('parsed')
track_dataframe.head()
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 1)
#track_dataframe.style
#print(track_dataframe.to_string())
print('hi')

"""import numpy as np
from sklearn.datasets import load_iris
import pandas as pd

# Loading irirs dataset
data = load_iris()
df = pd.DataFrame(data.data,
                  columns=data.feature_names)"""