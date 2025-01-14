# src/backend/services/vector_store_service.py

from typing import List
import numpy as np
from ..db.repository import get_embeddings

def search_relevant_chunks(user_question: str, top_k: int = 3) -> List[str]:
    """
    Ejemplo mock de búsqueda:
    1) Genera embedding de la pregunta
    2) Recupera todos los embeddings de la BD
    3) Calcula similitud coseno
    4) Retorna los textos con mayor similitud
    """
    question_embedding = generate_question_embedding(user_question)
    all_docs = get_embeddings()

    # Asumiendo que cada doc tiene doc["embedding"] como lista de float
    # Convertimos a np.array
    similarities = []
    for doc in all_docs:
        doc_vector = np.array(doc["embedding"])
        cos_sim = cosine_similarity(question_embedding, doc_vector)
        similarities.append((doc["original_text"], cos_sim))

    # Ordenar por similitud descendente
    similarities.sort(key=lambda x: x[1], reverse=True)

    # Retornar los top_k
    relevant_texts = [item[0] for item in similarities[:top_k]]
    return relevant_texts


def generate_question_embedding(text: str) -> np.ndarray:
    """
    Genera embedding para la pregunta usando la API de OpenAI
    o cualquier otra herramienta que estés usando.
    """
    import openai
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"
        )
        vector = response['data'][0]['embedding']
        return np.array(vector)
    except Exception as e:
        print(f"Error al generar embedding para la pregunta: {e}")
        return np.zeros(1536)  # tamaño del embedding de text-embedding-ada-002

def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    """
    Calcula la similitud coseno entre dos vectores NumPy.
    """
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)
