# src/backend/api/routes/chatbot_routes.py

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ..dependencies import get_db  # puedes crear un archivo dependencies.py para inyectar la DB
from ...services import conversation_service, crawler_service

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    source: str
    message_type: str
    conversation_id: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(chat_request: ChatRequest):
    """
    1) Recibe el mensaje del usuario
    2) Llama a GPT-4 con RAG
    3) Devuelve la respuesta generada
    """
    response_text = conversation_service.handle_chat(chat_request)
    return ChatResponse(response=response_text)


@router.get("/crawl")
async def crawl_endpoint():
    """
    1) Activa la función que extrae datos de la página web
    2) Genera embeddings con OpenAI
    3) Guarda todo en la BD
    """
    crawler_service.run_crawler()
    return {"message": "Crawling iniciado..."}
