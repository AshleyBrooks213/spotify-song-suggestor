"""Data visualization functions"""

from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px

router = APIRouter()


@router.get('/viz')
async def viz():
    """
    ### Response
    JSON string to render with [react-plotly.js](https://plotly.com/javascript/react/)
    """

    cols = ['acousticness',	'danceability', 'energy', 'instrumentalness', 'key',
        'liveness', 'loudness',	'popularity', 'speechiness', 'tempo', 'valence']
    
    df_plot = pd.read_csv('app/results.csv')
    
    # Make Plotly figure
    #fig = px.box(df_plot, orientation='v', column=columns, title='Strength of Song Characteristics')
    fig = gfp
    # Plotly figure for song results

    # Return Plotly figure as JSON string
    return fig.to_json()