"""Data visualization functions"""

from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import logging
import random
import pickle
import re

from fastapi import APIRouter, HTTPException
import numpy as np
from pydantic import BaseModel, Field, validator
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing
from pickle import dump

log = logging.getLogger(__name__)
router = APIRouter()

url = 'https://raw.githubusercontent.com/AshleyBrooks213/spotify-song-suggestor/main/app/results.csv'
predicted_songs = pd.read_csv(url)


@router.get('/viz')
async def viz(Predictions = predicted_songs):
    #"""
    ### Response
    #JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
    #"""

    #cols = ['acousticness',	'danceability', 'energy', 'instrumentalness', 'key',
    #    'liveness', 'loudness',	'popularity', 'speechiness', 'tempo', 'valence']
    
    #df_plot = pd.read_csv('app/results.csv')
    
    # Make Plotly figure
    #fig = px.box(df_plot, orientation='v', column=columns, title='Strength of Song Characteristics')
    #fig = gfp
    # Plotly figure for song results

    # Return Plotly figure as JSON string

    predicted_songs = predicted_songs
    
    def plot_songs_attributes_boxplots(df):

        fig = go.Figure()
        fig.add_trace(go.Box(x=df.acousticness, name='acousticness'))
        fig.add_trace(go.Box(x=df.danceability, name = "danceability"))
        fig.add_trace(go.Box(x=df.energy, name = "energy"))
        fig.add_trace(go.Box(x=df_predict.instrumentalness, name = "instrumentalness"))
        fig.add_trace(go.Box(x=df.key, name = "key"))
        fig.add_trace(go.Box(x=df.liveness, name = "liveness"))
        fig.add_trace(go.Box(x=df.loudness, name = "loudness"))
        fig.add_trace(go.Box(x=df.popularity, name = "popularity"))
        fig.add_trace(go.Box(x=df.speechiness, name = "speechiness"))
        fig.add_trace(go.Box(x=df.tempo, name = "tempo"))
        fig.add_trace(go.Box(x=df.valence, name = "valence"))
  
        fig.update_layout(title_text = 'Distribution of Predicted Songs\' Attributes')

        return fig
    
    predictions_graph = plot_songs_attributes_boxplots(predicted_songs)
    
    return predictions_graph.to_json()
