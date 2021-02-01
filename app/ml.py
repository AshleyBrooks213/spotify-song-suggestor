"""Machine learning functions"""

import logging
import random
import pickle

from fastapi import APIRouter, HTTPException
import pandas as pd
from pydantic import BaseModel, Field, validator


"""Load Model"""
# loaded_model = pickle.load(open"", 'rb')

"""Load vectorizer"""
# loaded_vectorizer = pickle.load(open("", 'rb'))

"""EDA GOES HERE"""


log = logging.getLogger(__name__)
router = APIRouter()


"""List of SONGS"""
# song_list = {}


"""LIST OF ANOTHER ATTRIBUTE FOR USER TO INPUT"""
# other_list = {}


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""
    # INCLUDE EXAMPLE HERE!
    x1: float = Field(..., example=3.14)
    x2: int = Field(..., example=-42)
    x3: str = Field(..., example='banjo')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `x1`: positive float
    - `x2`: integer
    - `x3`: string

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    """
    user_song_list = item.COLUMN_NAME_HERE.split(',')
    other_user_list = item.COLUMN_NAME_HERE.split(',')
    for song in user_song_list:
        if song not in song_list:
            raise HTTPException(status_code=404, detail=f'Song {song} not found')
    for other in other_user_list:
        if other not in other_user_list:
            raise HTTPException(status_code=404, detail=f'Other {other} not found')
    #X_new = item.to_df()
    #log.info(X_new)
    #y_pred = random.choice([True, False])
    #y_pred_proba = random.random() / 2 + 0.5
    #return {
    #    'prediction': y_pred,
    #    'probability': y_pred_proba
    #}
