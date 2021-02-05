"""Data visualization functions"""

import logging
from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from app import model
from model import df_nn

log = logging.getLogger(__name__)
router = APIRouter()

#df_results = pd.read_csv('app/results.csv')
df_results=df_nn

@router.get('/viz')
async def viz(df=df_results):
    """
    ### Response
    JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
    """

    #cols = ['acousticness',	'danceability', 'energy', 'instrumentalness', 'key',
    #    'liveness', 'loudness',	'popularity', 'speechiness', 'tempo', 'valence']
    #fig = go.Figure()
    #fig.add_trace(go.Box(x=df['acousticness'], name='acousticness'))
    # fig.add_trace(go.Box(x=df.danceability, name = "danceability"))
    # fig.add_trace(go.Box(x=df.energy, name = "energy"))
    # fig.add_trace(go.Box(x=df.instrumentalness, name = "instrumentalness"))
    # fig.add_trace(go.Box(x=df.key, name = "key"))
    # fig.add_trace(go.Box(x=df.liveness, name = "liveness"))
    # fig.add_trace(go.Box(x=df.loudness, name = "loudness"))
    # fig.add_trace(go.Box(x=df.popularity, name = "popularity"))
    # fig.add_trace(go.Box(x=df.speechiness, name = "speechiness"))
    # fig.add_trace(go.Box(x=df.tempo, name = "tempo"))
    # fig.add_trace(go.Box(x=df.valence, name = "valence"))
    
    #fig.update_layout(title_text = 'Distribution of Predicted Songs\' Attributes')

    return df