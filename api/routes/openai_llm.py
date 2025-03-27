from fastapi import APIRouter, Depends
from schemas.llm import PromptRequest, PromptResponse
from services.llm_logic import answer_bot
from db.session import get_db
import random
from sqlalchemy.orm import Session
from llm.openai_client import generate_response
from models.models import Questions

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post('/answer', response_model=PromptResponse)

def answer(prompt: PromptRequest):
    reply = answer_bot(prompt.text)
    return PromptResponse(reply=reply)

@router.get("/ask-question")
def ask_llm_a_question(db: Session=Depends(get_db)):
    # questions = db.query(Questions).all()
    questions = db.query(Questions).order_by(Questions.Id.desc()).first()

    if not questions:
        return {"reply: No questions found in the database"}
    # question = random.choice(questions)
    prompt = f"You are a helpful assistant. Ask the user five similar question like this:\n\n{questions.question_text}"
    print(prompt)
    response = generate_response(prompt)

    return{"reply" : response}