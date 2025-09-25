from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .answer import AnswerResponse


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
