from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_prediction():
    response = client.post(
        "/predict",
        json={
            "gender": "female",
            "race_ethnicity": "group B",
            "parental_level_of_education": "bachelor's degree",
            "lunch": "standard",
            "math_score": 70,
            "reading_score": 72,
            "writing_score": 68
        }
    )

    assert response.status_code == 200
    assert "prediction" in response.json()