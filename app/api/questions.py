from app import schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..schemas import QuestionResponse

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=list[QuestionResponse])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    questions = crud.get_questions(db, skip=skip, limit=limit)
    return questions


@router.post("/", response_model=schemas.QuestionResponse)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    if not question.text.strip():
        raise HTTPException(status_code=400, detail="Question text cannot be empty")
    return crud.create_question(db=db, question=question)


@router.get("/{id}", response_model=schemas.QuestionResponse)
def read_question(id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id=id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.delete("/{id}")
def delete_question(id: int, db: Session = Depends(get_db)):
    success = crud.delete_question(db, question_id=id)
    if not success:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted successfully"}
