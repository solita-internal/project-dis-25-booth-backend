from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crude import responses as crud
from schemas.responses import ResponseCreate, ResponseRead

router = APIRouter(prefix="/response", tags=["Responses"])
@router.post("/", response_model=ResponseRead)
def create_response(data: ResponseCreate, db: Session=Depends(get_db)):
    return crud.create_response(db, data)
