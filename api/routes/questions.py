from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud import questions as crud
from schemas.questions import QuestionsCreate, QuestionsRead

router = APIRouter(prefix="/question", tags=["Questions"])
@router.post("/", response_model=QuestionsRead)
def create_question(data: QuestionsCreate, db: Session=Depends(get_db)):
    return crud.create_question(db, data)

## create a function for fetching questions (LLM comes in (i guess))

@router.get('/{question_id}', response_model=QuestionsRead)
def get_question(question_id: int, db: Session=Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question: 
        raise HTTPException(status_code=404, detail="Question not found")
    return question