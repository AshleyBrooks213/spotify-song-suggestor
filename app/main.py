from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz, ml2, model

description = """
This web app is designed to predict the top 10 songs a user may be interested in,
a list of artists, and a dataframe that contains all of the information associated 
with the predictions. 
In order to base your prediction on a different artist, simply look at the list, 
find the artist you want and the number associated with it, and plug the number
into the model artist query.
Doing this will change the prediction outcome.
You can also change the song title in the model song query.
To use these interactive docs:
- Click on an endpoint below (Model)
- Click the **Try it out** button
- Input song title and the number of the artist you would like to base
    your returned predictions on.
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
\n
\n
Created by: 
Nicholas Adamski - Ashley Brooks - Ricky Chance - Shannon Li
"""

app = FastAPI(
    title='Spotify Song Suggestor',
    description=description,
    docs_url='/',
)

#app.include_router(db.router, tags=['Database'])
#app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])
#app.include_router(ml2.router, tags=['Machine Learning 2'])
app.include_router(model.router, tags=['Model'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
