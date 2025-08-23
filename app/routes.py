from fastapi import APIRouter
from pydantic import BaseModel
from app.utils import generate_and_upload

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate(prompt_request: PromptRequest):
    video_url = generate_and_upload(prompt_request.prompt)
    return {"video_url": video_url}