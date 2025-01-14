# src/backend/services/crawler_service.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .openai_service import get_completion
from ..db.repository import create_embedding

def run_crawler():
    """
    1) Descarga el contenido de la página
    2) Procesa el HTML y extrae texto
    3) Divide en chunks
    4) Genera embeddings con OpenAI
    5) Inserta embeddings en la BD
    """
    url = "https://www.medellin.gov.co/"
    print(f"Iniciando crawling en: {url}")

    # 1) Descarga el contenido
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error al descargar la página: {response.status_code}")
        return

    # 2) Procesar HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # Podrías extraer <p>, <h1>, <h2>, etc.
    all_paragraphs = soup.find_all(['p', 'h1', 'h2'])

    # 3) Dividir en chunks simples (aquí un ejemplo muy básico)
    text_chunks = []
    for tag in all_paragraphs:
        text = tag.get_text(strip=True)
        if text:
            text_chunks.append(text)

    # 4) Generar embeddings y 5) Guardar en la BD
    for chunk in text_chunks:
        embedding_vector = generate_embedding(chunk)
        create_embedding({
            "original_text": chunk,
            "embedding": embedding_vector,
            "source_url": url,
            "created_at": datetime.utcnow(),
            "title": "Información Extraída"  # O lo que consideres
        })

    print("Crawling finalizado.")


def generate_embedding(text: str):
    """
    Ejemplo sencillo para obtener embedding usando la API de OpenAI.
    """
    import openai
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"  # Modelo de embeddings de OpenAI
        )
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Error al generar embedding: {e}")
        return []
