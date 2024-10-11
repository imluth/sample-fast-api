#importing required libraries
from fastapi import FastAPI # type: ignore
import random

app = FastAPI()

#setting up app routes
@app.get('/')
async def root():
    return {'example': 'This is example', 'data': 999}

#main function of the API
@app.get('/random')
async def get_random():
    rn: int = random.randint(0, 100)
    return {'number': rn, 'limit': 100}

