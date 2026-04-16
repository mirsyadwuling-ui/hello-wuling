from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Wuling AI Backend Ready 🚀"}

@app.post("/api/chat")
async def chat(req: ChatRequest):
    user_input = req.message

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Anda teknisi Wuling. Jawab seperti teknisi profesional."},
            {"role": "user", "content": user_input}
        ]
    )

    return {"response": completion.choices[0].message.content}