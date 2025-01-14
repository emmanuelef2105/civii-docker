# src/backend/db/models.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageModel(BaseModel):
    user_id: str
    text: str
    message_type: str
    emotion: Optional[str] = None
    timestamp: datetime = datetime.utcnow()

class EmbeddingModel(BaseModel):
    original_text: str
    embedding: list
    source_url: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    title: Optional[str] = None
