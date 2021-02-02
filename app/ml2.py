"""Machine learning functions"""

import logging
import random
import pickle
import re

from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field, validator
from sklearn.neighbors import NearestNeighbors
from pickle import dump

"""Load Model"""
# loaded_model = pickle.load(open"", 'rb')

log = logging.getLogger(__name__)
router = APIRouter()


#dump(model, 'model_knn.pkl', compress=True)


url = 'https://raw.githubusercontent.com/boscolio/spotify_data/main/spotify.csv'

@router.get("/pickler")
async def pickle_model(url):
    df = pd.read_csv(url, index_col=[0])
    df = df.copy()
    model = NearestNeighbors(n_neighbors=11)
    model.fit(df[df.columns[2:13]])

    knn_file = open('model_knn.pkl', 'wb') # create file
    pickle.dump(model, knn_file, compress=True) # dumps model into file
    #dump(model, 'model_knn.pkl', compress=True)

    return model, knn_file, df



# model = pickle_model(url)[0]
# pickle_file = pickle_model(url)[1]
# df = pickle_model(url)[2]


@router.get("/predict")
async def NN_predict(track, artist=0): 
    model, pickle_file, df = pickle_model(url)

    knn_file = open('/app/api/model_knn.pkl', 'rb') # read only version
    model_knn = pickle.load(knn_file) # testing loading byte str

    # Assigned input matches to a series
    obs = df.index[df['name'] == track]
    series = df.iloc[obs, 2:13].to_numpy()

    # Query model based on input
    neighbors = model_knn.kneighbors(series)
    new_obs = neighbors[1][artist][1:11]

    # Display artist and spotify id of all songs that match the input
    artist_list = df.iloc[obs, 1]

    # Using spotify track id to return dataframe of results
    df_nn = df.loc[new_obs]

    names = df_nn[['name', 'artists']]
    names_dict = names.to_dict(orient='records')
    
    #print(artist_list)
    return names_dict, artist_list, df_nn