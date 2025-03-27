
from fastapi import FastAPI
from api.routes import survey_session, responses, questions, openai_llm

from models import models
app = FastAPI()
app.include_router(survey_session.router)
app.include_router(responses.router)
app.include_router(questions.router)
app.include_router(openai_llm.router)

