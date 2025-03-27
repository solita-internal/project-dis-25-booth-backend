from llm.openai_client import generate_response
from llm.prompts import format_prompt

def answer_bot(user_input: str) -> str: 
    prompt = format_prompt(user_input)
    return generate_response(prompt)