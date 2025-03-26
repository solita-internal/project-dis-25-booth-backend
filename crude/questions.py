from models.models import Questions
from schemas.questions import QuestionsCreate
from sqlalchemy.orm import Session

def create_question(db: Session, question: QuestionsCreate ) -> Questions:
    db_obj = Questions(**question.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj


