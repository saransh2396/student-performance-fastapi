from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

from app.schemas.student_schema import StudentInput
from app.utils.logger import logger

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH", "artifacts/model.pkl")
APP_NAME = os.getenv("APP_NAME", "Student Performance API")

# -----------------------------
# Initialize FastAPI App
# -----------------------------
app = FastAPI(title=APP_NAME)

# -----------------------------
# Load Model at Startup
# -----------------------------
try:
    model = joblib.load(MODEL_PATH)
    logger.info(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    logger.error(f"Model loading failed: {e}")
    raise RuntimeError("Model could not be loaded.")


# -----------------------------
# Health Check Endpoint
# -----------------------------
@app.get("/")
def home():
    logger.info("Health check endpoint called")
    return {"message": f"{APP_NAME} is running"}


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(data: StudentInput):

    try:
        input_data = data.model_dump()   # Pydantic v2 safe method
        logger.info(f"Received input: {input_data}")

        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]

        # Get probability of predicted class properly
        class_index = list(model.classes_).index(prediction)
        predicted_prob = probabilities[class_index]

        logger.info(
            f"Prediction: {prediction}, Probability: {predicted_prob}"
        )

        return {
            "prediction": prediction,
            "probability": round(float(predicted_prob), 4)
        }

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )