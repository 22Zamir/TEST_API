from sqlalchemy.orm import Session
from ..models.question import Question
from ..schemas.question import QuestionCreate


def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Question).offset(skip).limit(limit).all()


def create_question(db: Session, question: QuestionCreate):
    db_question = Question(text=question.text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int):
    question = db.query(Question).filter(Question.id == question_id).first()
    if question:
        db.delete(question)
        db.commit()
        return True
    return False
