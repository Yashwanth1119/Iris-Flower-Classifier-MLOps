from fastapi import Fastapi
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_widrth: float

@app.posst("/predict") 
def get_prediction(data: IrisInput):
    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_width
    ]
    prediction = predict(features)
    return {"prediction": int(prediction)}
