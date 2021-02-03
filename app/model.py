import logging
import random
import pickle
import re

from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel, Field, validator
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing
from pickle import dump

log = logging.getLogger(__name__)
router = APIRouter()

url = 'https://raw.githubusercontent.com/boscolio/spotify_data/main/spotify.csv'

df = pd.read_csv(url, index_col=[0])
model = NearestNeighbors(n_neighbors=11)
model.fit(df[df.columns[2:13]])


@router.get("/model")
async def predict(song='Float On', artist=0):

    # Assign input matches to a series
    obs = df.index[df['name'] == song]
    series = df.iloc[obs, 2:13].to_numpy()

    # Query model based on input
    #artist = int(artist)
    neighbors = model.kneighbors(series)
    new_obs = neighbors[1][int(artist)][1:11]

    # Display artist and spotify id of all songs that match the input
    artist_list = df.iloc[obs, 1]

    # Using spotify track id to return dataframe of results
    df_nn = df.loc[new_obs]
    # Assign songs and artists to a dictionary
    names = df_nn[['name', 'artists']]
    names_dict = names.to_dict(orient='records')

    return names_dict, artist_list, df_nn