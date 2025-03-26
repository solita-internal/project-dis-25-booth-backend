from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SurveySessionBase(BaseModel):
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    contact_opt_in: Optional[bool] = None
    name: Optional[str] = None
    email: Optional[str] = None
    organization: Optional[str] = None
    location: Optional[str] = None

class SurveySessionCreate(SurveySessionBase):
    pass

class SurveySessionUpdate(SurveySessionBase):
    pass

class SurveySessionRead(SurveySessionBase):
    Id: int #primary key

    class Config:
        from_attributes = True