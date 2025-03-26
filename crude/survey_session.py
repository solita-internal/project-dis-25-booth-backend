from sqlalchemy.orm import Session
from models.models import SurveySession
from schemas.survey_session import SurveySessionCreate
def create_survey_session(db: Session, survey: SurveySessionCreate) -> SurveySession: 
    db_obj = SurveySession(**survey.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    
    return db_obj