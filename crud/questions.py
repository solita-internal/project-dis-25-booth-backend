from models.models import Questions
from schemas.questions import QuestionsCreate, QuestionsRead
from sqlalchemy.orm import Session

def create_question(db: Session, question: QuestionsCreate ) -> Questions:
    db_obj = Questions(**question.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj

def get_question(db: Session, question_id: int) -> Questions:
    db_obj = db.query(Questions).filter(Questions.Id == question_id).first()
    return db_obj


