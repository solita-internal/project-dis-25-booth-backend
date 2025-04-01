from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ConversationTurnCreate(BaseModel):
    role: str 
    message: str 
    consent_to_contact : Optional[bool] = None
    guest_name : Optional[str] = None
    company : Optional[str] = None 
    email : Optional[EmailStr] = None

class ConversationTurnResponse(ConversationTurnCreate):
    id: int
    timestamp: datetime
    class Config:
        model_config = True
        



