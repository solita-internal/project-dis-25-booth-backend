
from fastapi import FastAPI
from api.routes import survey_session, responses, questions

from models import models
app = FastAPI()
app.include_router(survey_session.router)
app.include_router(responses.router)
app.include_router(questions.router)
