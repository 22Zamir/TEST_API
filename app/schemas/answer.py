from pydantic import BaseModel
from datetime import datetime


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
