import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/stud.csv")

# -----------------------------
# Define Features & Target
# -----------------------------
X = df.drop("test_preparation_course", axis=1)
y = df["test_preparation_course"]

# -----------------------------
# Categorical & Numerical Columns
# -----------------------------
categorical_cols = [
    "gender",
    "race_ethnicity",
    "parental_level_of_education",
    "lunch"
]

numerical_cols = [
    "math_score",
    "reading_score",
    "writing_score"
]

# -----------------------------
# Preprocessing
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

# -----------------------------
# Create Pipeline
# -----------------------------
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model.fit(X_train, y_train)

# -----------------------------
# Evaluate
# -----------------------------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
os.makedirs("artifacts", exist_ok=True)
joblib.dump(model, "artifacts/model.pkl")

print("Model saved successfully!")