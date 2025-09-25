from sqlalchemy.orm import Session
from ..models.answer import Answer
from ..schemas.answer import AnswerCreate


def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.id == answer_id).first()


def create_answer(db: Session, answer: AnswerCreate, question_id: int):
    db_answer = Answer(
        question_id=question_id,
        user_id=answer.user_id,
        text=answer.text
    )
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def delete_answer(db: Session, answer_id: int):
    answer = db.query(Answer).filter(Answer.id == answer_id).first()
    if answer:
        db.delete(answer)
        db.commit()
        return True
    return False
