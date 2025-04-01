from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from models.models import ConversationTurns
from datetime import datetime
from schemas.ConversationTurn import ConversationTurnCreate
from llm.openai_client import generate_response
from services.llm_logic import build_prompt, extract_summary_from_conversation
router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/start")

def start_conversation(db: Session = Depends(get_db)):

    intro_message = (
        "Hi there! I'm Ava, your AI host at the conference 👋 "
        "Before we start, I want to be fully transparent. "
        "To follow GDPR guidelines, I’d like to ask for your consent to store your answers for analysis. "
        "This helps us understand how companies like yours are using AI — but it’s 100'%' optional. "
        "Would you like to continue and share your thoughts with us? "
        "👉 Please type 'yes' to give consent, or 'no' to continue anonymously."
    )
    new_session = ConversationTurns(
        role="ai",
        message=intro_message,
        timestamp=datetime.utcnow()
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    
    return {
        "session_id":new_session.id,
        "reply": intro_message
    }

@router.post("/next-message")

def continue_conversation(user_input: ConversationTurnCreate, db: Session = Depends(get_db)):
    user_text = user_input.message.strip().lower()

    user_turn = ConversationTurns(role="user", message=user_input.message)
    db.add(user_turn)
    db.commit()

    last_ai_turn = db.query(ConversationTurns).filter(ConversationTurns.role=="ai").order_by(ConversationTurns.timestamp.desc()).first()
    last_step = last_ai_turn.step if last_ai_turn and last_ai_turn.step else "gdpr_consent"

    next_step = None
    ai_message = ""

    if last_step == "gdpr_consent":
        if user_text in ["yes", "i agree", "sure"]:
            next_step = "ask_name"
            ai_message = "Great! What's your name?"
        elif user_text in ["no", "nope"]:
            next_step = "ai_questions"
            ai_message = "No worries — let’s dive in! First off, how is your company using AI?"
        else:
            next_step = "gdpr_consent"
            ai_message = "Just to confirm — do you consent to us storing your responses? Type 'yes' or 'no'."
    elif last_step == "ask_name": 
        save_name = ConversationTurns(guest_name=user_input.message)
        next_step = "ask_company"
        ai_message = "Thanks! And which company are you with?"
    elif last_step == "ask_company": 
        next_step = "ask_email"
        ai_message = "Optional — What is your email? 😄"
    elif last_step == "ask_email":
        next_step = "ai_questions"
        ai_message = "Awesome. Let’s get started — how is your company currently using AI?"
    
    elif last_step == "ai_questions":
        print("here now")
        recent_turns = db.query(ConversationTurns).filter(ConversationTurns.role=="user").order_by(ConversationTurns.timestamp.desc()).limit(5).all()
        context = [t.message for t in reversed(recent_turns)]
        conversation_summary = extract_summary_from_conversation(context)
        prompt = build_prompt(conversation_summary)
        ai_message = generate_response(prompt)
        next_step = "ai_questions"
    print(next_step)
    ai_turn = ConversationTurns(role="ai", message=ai_message, step=next_step)
    db.add(ai_turn)
    db.commit()

    return {"reply": ai_message}