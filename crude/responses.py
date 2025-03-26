from models.models import Responses
from schemas.responses import ResponseCreate
from sqlalchemy.orm import Session

def create_response(db: Session, response: ResponseCreate ) -> Responses:
    db_obj = Responses(**response.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj


