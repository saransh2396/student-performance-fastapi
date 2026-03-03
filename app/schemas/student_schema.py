from pydantic import BaseModel, Field
from typing import Literal


class StudentInput(BaseModel):
    gender: Literal["male", "female"]
    race_ethnicity: str
    parental_level_of_education: str
    lunch: Literal["standard", "free/reduced"]
    math_score: int = Field(..., ge=0, le=100)
    reading_score: int = Field(..., ge=0, le=100)
    writing_score: int = Field(..., ge=0, le=100)