import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv

load_dotenv()

def generate_response(prompt: str) -> str:
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800)
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ OpenAI API error: {str(e)}"
