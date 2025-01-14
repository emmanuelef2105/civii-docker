# src/backend/services/openai_service.py

import os
import openai
from typing import List

# Carga la API KEY desde variables de entorno
openai.api_key = os.getenv("OPENAI_API_KEY", "TU_API_KEY")

def get_completion(messages: List[dict], model: str = "gpt-4", temperature: float = 0.7) -> str:
    """
    Envía un listado de mensajes a la API de OpenAI y retorna la respuesta.

    :param messages: Lista de diccionarios con 'role' y 'content'.
    :param model: Modelo a utilizar (p.ej. 'gpt-3.5-turbo', 'gpt-4').
    :param temperature: Control de aleatoriedad en la respuesta.
    :return: Cadena de texto con la respuesta del modelo.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error llamando a OpenAI: {e}")
        return "Lo siento, hubo un error al procesar la solicitud."
