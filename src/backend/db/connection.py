# src/backend/db/connection.py

import os
from pymongo import MongoClient

# Este archivo se encarga de la conexión a MongoDB
# Puedes usar variables de entorno para el host, puerto, usuario y contraseña
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASS = os.getenv("MONGO_PASS", "example")

def get_database():
    """
    Retorna la base de datos con la que vamos a trabajar.
    """
    # Formamos la URI de conexión. Asume que la autenticación es opcional.
    uri = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/"

    client = MongoClient(uri)
    
    # Elige el nombre de tu BD. Por ejemplo, 'civii_db'
    db = client['civii_db']
    return db
