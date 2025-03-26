from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ResponsesBase(BaseModel):

    session_id: Optional[int] = None
    question_id: Optional[int] = None
    answer_text: Optional[str] = None
    timestamp: Optional[datetime] = None

class ResponseCreate(ResponsesBase): 
    pass 
class ResponseUpdate(ResponsesBase):
    pass 

class ResponseRead(ResponsesBase): 
    Id : int

    class Config: 
        from_attributes = True

