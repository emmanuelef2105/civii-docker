# src/backend/services/emotion_service.py

def detect_emotion(text: str) -> str:
    """
    Ejemplo simple para detectar emoción.
    En la práctica, podrías usar un modelo de clasificación
    (por ejemplo, transformadores de huggingface).
    """
    # Reglas muy sencillas:
    if "feliz" in text or "contento" in text:
        return "alegría"
    if "triste" in text:
        return "tristeza"
    if "enojado" in text or "molesto" in text:
        return "enojo"
    # ...
    return "neutral"
