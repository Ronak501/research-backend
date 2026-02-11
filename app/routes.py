from fastapi import APIRouter
from pydantic import BaseModel
from app.model import generate_text

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 50

@router.post("/generate")
def generate(request: PromptRequest):
    output = generate_text(request.prompt, request.max_length)
    return {
        "input": request.prompt,
        "output": output
    }
