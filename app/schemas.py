from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


# --- Схемы для Answer ---
class AnswerCreate(BaseModel):
    user_id: str
    text: str

    class Config:
        from_attributes = True


class AnswerResponse(BaseModel):
    id: int
    question_id: int
    user_id: str
    text: str
    created_at: datetime

    class Config:
        from_attributes = True


# --- Схемы для Question ---
class QuestionCreate(BaseModel):
    text: str

    class Config:
        from_attributes = True


class QuestionResponse(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[AnswerResponse] = []

    class Config:
        from_attributes = True
