# Student Performance – Test Preparation Prediction API

## 📌 Project Overview

This project builds a Machine Learning classification model to predict whether a student has completed a **test preparation course** based on demographic and academic performance features.

The trained model is deployed using **FastAPI**, providing a production-ready REST API for inference.

---

## 🚀 Problem Statement

Given the following student attributes:

* gender
* race_ethnicity
* parental_level_of_education
* lunch
* math_score
* reading_score
* writing_score

Predict:

> 🎯 **test_preparation_course** (completed / none)

This is a supervised binary classification problem.

---

## 🧠 Machine Learning Pipeline

The project follows a production-style ML workflow:

1. Data Cleaning & Preprocessing
2. Feature Encoding (Categorical → Numerical)
3. Model Training (Scikit-learn)
4. Model Serialization using Joblib
5. API Deployment using FastAPI

---

## 📂 Project Structure

```
student_performance_api/
│
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── preprocessing/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── data/
│   └── student_data.csv
│
├── notebook/
│   └── training.ipynb
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-performance-fastapi.git
cd student-performance-fastapi
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Swagger UI Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📬 Sample Prediction Request

### POST `/predict`

```json
{
  "gender": "female",
  "race_ethnicity": "group B",
  "parental_level_of_education": "bachelor's degree",
  "lunch": "standard",
  "math_score": 72,
  "reading_score": 74,
  "writing_score": 70
}
```

### Response

```json
{
  "prediction": "completed"
}
```

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* Uvicorn
* Joblib

---

## 🧩 Future Improvements

* Docker containerization
* CI/CD integration
* Model monitoring
* Cloud deployment (AWS / Azure)
* Logging & request tracking

---

## 👤 Author

Saransh Srivastava
Data Science | Machine Learning | MLOps

---

## ⭐ If You Found This Useful

Consider giving this repository a star!
