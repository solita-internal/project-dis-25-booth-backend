from pydantic import BaseModel
from typing import Optional

class QuestionsBase(BaseModel):
    question_text : Optional[str] = None
    category : Optional[str] = None
    order : Optional[int] = None
    active : Optional[bool] = None

class QuestionsCreate(QuestionsBase):
    pass

class QuestionsUpdate(QuestionsBase):
    pass

class QuestionsRead(QuestionsBase):
    Id: int

    class Config:
        from_attributes = True
