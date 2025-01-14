# src/backend/services/langchain_service.py

from .vector_store_service import search_relevant_chunks
from .openai_service import get_completion

def generate_answer_with_rag(user_question: str) -> str:
    """
    1) Busca en la base de datos/vector store los chunks más relevantes.
    2) Crea un prompt que incluya esos chunks como contexto.
    3) Llama a GPT-4 (u otro modelo) para generar la respuesta final.
    4) Devuelve la respuesta.
    """
    # 1) Recuperar contexto relevante
    relevant_chunks = search_relevant_chunks(user_question)

    # 2) Construir el prompt
    # Podrías formatear los chunks como bullet points o párrafos
    context_text = "\n".join([f"- {chunk}" for chunk in relevant_chunks])

    system_prompt = "Eres un asistente experto en RAG. Usa la información que te proporciono para dar respuestas precisas."

    user_prompt = f"""
    Pregunta del usuario: "{user_question}"
    Contexto relevante:
    {context_text}

    Por favor, responde utilizando el contexto anterior. 
    Si no está en el contexto, admite que no tienes esa información.
    """

    # 3) Llamar a GPT-4 (u otro modelo)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    answer = get_completion(messages=messages, model="gpt-4", temperature=0.7)
    return answer
