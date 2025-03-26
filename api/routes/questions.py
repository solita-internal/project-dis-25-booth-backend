from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crude import questions as crud
from schemas.questions import QuestionsCreate, QuestionsRead

router = APIRouter(prefix="/question", tags=["Questions"])
@router.post("/", response_model=QuestionsRead)
def create_question(data: QuestionsCreate, db: Session=Depends(get_db)):
    return crud.create_question(db, data)
