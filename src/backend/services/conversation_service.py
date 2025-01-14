# src/backend/services/conversation_service.py

from ..db.repository import create_message
from .langchain_service import generate_answer_with_rag
from .openai_service import get_completion  # si quisieras usarlo directamente
from .emotion_service import detect_emotion  # si usas análisis de emociones

def handle_chat(chat_request):
    """
    Maneja el flujo de la conversación:
    1) Guarda el mensaje del usuario en la BD.
    2) Genera una respuesta usando RAG (o GPT-4 directo).
    3) Guarda la respuesta del chatbot en la BD.
    4) Retorna la respuesta para enviarla al frontend.
    """
    user_message = chat_request.message
    user_id = chat_request.user_id

    # 1) Guarda el mensaje del usuario
    create_message({
        "user_id": user_id,
        "text": user_message,
        "message_type": "usuario",
        "emotion": detect_emotion(user_message),  # Opcional, si integras emotion_service
    })

    # 2) Genera la respuesta con RAG
    response_text = generate_answer_with_rag(user_message)

    # 3) Guarda la respuesta del chatbot
    create_message({
        "user_id": user_id,
        "text": response_text,
        "message_type": "chatbot",
        # "emotion": detect_emotion(response_text), # Opcional
    })

    # 4) Regresamos la respuesta
    return response_text
