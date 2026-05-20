from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from core.agent import run_agent
from core.voice import speak

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Request(BaseModel):
    message: str
    speak_output: bool = True


@app.post("/chat")
def chat(req: Request):

    response = run_agent(req.message)

    if req.speak_output:
        speak(response)

    return {
        "input": req.message,
        "response": response
    }
