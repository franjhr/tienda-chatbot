from fastapi import APIRouter, HTTPException

from api.schemas.chat import ChatRequest, ChatResponse
from services.chatbot import ChatbotUnavailable, respond

router = APIRouter()


@router.post("/chat")
def chat(chat_request: ChatRequest) -> ChatResponse:
    try:
        return ChatResponse(response=respond(chat_request.message))
    except ChatbotUnavailable as error:
        raise HTTPException(status_code=503, detail="Chatbot no disponible") from error
