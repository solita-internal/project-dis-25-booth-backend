from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crude import survey_session as crud
from schemas.survey_session import SurveySessionCreate, SurveySessionRead

router = APIRouter(prefix="/survey-sessions", tags=["Survey Session"])

@router.post("/", response_model=SurveySessionRead)

def create_session(data: SurveySessionCreate, db: Session=Depends(get_db)):
    return crud.create_response(db, data)
