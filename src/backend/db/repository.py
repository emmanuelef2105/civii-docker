# src/backend/db/repository.py

from datetime import datetime
from .connection import get_database

db = get_database()

########################
#      EMBEDDINGS      #
########################

def create_embedding(document):
    """
    Crea un nuevo embedding en la colección `embeddings`.
    """
    document['created_at'] = datetime.utcnow()
    return db.embeddings.insert_one(document).inserted_id

def get_embeddings(query={}):
    """
    Obtiene embeddings según una consulta.
    query es un diccionario para filtrar resultados en MongoDB.
    """
    return list(db.embeddings.find(query))

def update_embedding(embedding_id, update_fields):
    """
    Actualiza un embedding por su _id.
    """
    from bson.objectid import ObjectId
    result = db.embeddings.update_one(
        {"_id": ObjectId(embedding_id)},
        {"$set": update_fields}
    )
    return result.modified_count

def delete_embedding(embedding_id):
    """
    Elimina un embedding por su _id.
    """
    from bson.objectid import ObjectId
    result = db.embeddings.delete_one({"_id": ObjectId(embedding_id)})
    return result.deleted_count


########################
#       MESSAGES       #
########################

def create_message(message):
    """
    Crea un nuevo mensaje en la colección `messages`.
    """
    message['timestamp'] = datetime.utcnow()
    return db.messages.insert_one(message).inserted_id

def get_messages(query={}, limit=0):
    """
    Obtiene mensajes según una consulta y un límite opcional.
    """
    if limit > 0:
        return list(db.messages.find(query).sort("timestamp", -1).limit(limit))
    else:
        return list(db.messages.find(query))

def update_message(message_id, update_fields):
    """
    Actualiza un mensaje por su _id.
    """
    from bson.objectid import ObjectId
    result = db.messages.update_one(
        {"_id": ObjectId(message_id)},
        {"$set": update_fields}
    )
    return result.modified_count

def delete_message(message_id):
    """
    Elimina un mensaje por su _id.
    """
    from bson.objectid import ObjectId
    result = db.messages.delete_one({"_id": ObjectId(message_id)})
    return result.deleted_count
