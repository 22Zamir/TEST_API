from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(prefix="/answers", tags=["answers"])


@router.post("/questions/{id}/answers/", response_model=schemas.AnswerResponse)
def create_answer_for_question(
        id: int,
        answer: schemas.AnswerCreate,
        db: Session = Depends(get_db)
):
    question = crud.get_question(db, question_id=id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    if not answer.text.strip():
        raise HTTPException(status_code=400, detail="Answer text cannot be empty")
    return crud.create_answer(db=db, answer=answer, question_id=id)


@router.get("/{id}", response_model=schemas.AnswerResponse)
def read_answer(id: int, db: Session = Depends(get_db)):
    db_answer = crud.get_answer(db, answer_id=id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer


@router.delete("/{id}")
def delete_answer(id: int, db: Session = Depends(get_db)):
    success = crud.delete_answer(db, answer_id=id)
    if not success:
        raise HTTPException(status_code=404, detail="Answer not found")
    return {"message": "Answer deleted successfully"}
