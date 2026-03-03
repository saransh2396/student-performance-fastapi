from fastapi import FastAPI
import joblib
import pandas as pd
from app.schemas.student_schema import StudentInput

app = FastAPI()

# Load trained model
model = joblib.load("artifacts/model.pkl")


@app.get("/")
def home():
    return {"message": "Student Performance Prediction API is running"}


@app.post("/predict")
def predict(data: StudentInput):

    # Convert input to dataframe
    input_df = pd.DataFrame([data.dict()])

    prediction = model.predict(input_df)[0]

    return {
        "prediction": prediction
    }