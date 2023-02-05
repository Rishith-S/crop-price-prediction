from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd

app = FastAPI()



class Inputs(BaseModel):
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int


@app.get('/')
def home():
    return 'hello'

@app.post("/ml-model")
async def ml_model(values: Inputs):
    data=values.dict()
    model = pickle.load(open("price_prediction.sav", 'rb'))
    y=model.predict([[data['a'],data['b'],data['c'],data['d'],data['e'],data['f']]]).tolist()
    return {
        'Result' : int(y[0])
    }


if __name__=='__main__':
    uvicorn.run('main:app',host='0.0.0.0',port=8001,log_level="info")