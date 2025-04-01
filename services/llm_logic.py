from llm.openai_client import generate_response
from llm.prompts import format_prompt
import json

def answer_bot(user_input: str) -> str: 
    prompt = format_prompt(user_input)
    return generate_response(prompt)

def greet_bot(user_input: str) -> str:
    prompt = format_prompt(user_input)
    return generate_response(prompt)

def extract_summary_from_conversation(conversation: list[str]) -> str: 
    history = "\n".join(f"{msg}" for msg in conversation)

    system_prompt = (
        "You're an AI assistant. Given the following conversation with a guest, extract a summary of what you know so far "
        "in structured JSON format with the fields: guest_name, company, ai_use_case, challenge, future_plan.\n"
        "If you don't know something, use null.\n\n"
        f"Conversation:\n{history}\n\n"
        "Respond ONLY with JSON in this format:\n"
        "{\n"
        "  \"guest_name\": ..., \n"
        "  \"company\": ..., \n"
        "  \"ai_use_case\": ..., \n"
        "  \"challenge\": ..., \n"
        "  \"future_plan\": ...\n"
        "}"
    )

    response = generate_response(system_prompt)

    try:
        summary = json.loads(response)
    except Exception:
        summary = {
            "guest_name": None,
            "company": None,
            "ai_use_case": None,
            "challenge": None,
            "future_plan": None
        }

    return summary

def build_prompt(conversation_summary: dict) -> str: 
    
    intro = (
        "You are Ava working at Solita, an AI interviewer at a tech conference. "
        "You're having a 1:1 conversation with a guest to understand how their company uses AI, "
        "what challenges they face, and their future plans. You are warm, curious, and sound like a professional interviewer."
    )

    # what she knows
    summary = "\n".join(
        f"- {key.replace('_', ' ').title()}: {value}" 
        for key, value in conversation_summary.items() 
        if value and isinstance(value, str)
    )
    print(summary)

    guidance = (
        "\n\nUsing what you've learned so far, ask the next relevant question. "
        "Avoid repeating questions. Ask only one short, clear question. "
        "If the conversation is wrapping up, you may offer to collect an email for a giveaway (optional for the guest)."
    )

    return f"{intro}\n\nYou’ve already learned:\n{summary}{guidance}"