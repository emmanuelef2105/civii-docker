# src/backend/app.py
import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Carga variables de entorno desde un archivo .env si lo deseas
load_dotenv()

app = FastAPI()

# Importa tus rutas
from .api.routes.chatbot_routes import router as chatbot_router

# Incluye las rutas en tu aplicación
app.include_router(chatbot_router, prefix="/api", tags=["Chatbot"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de CIVii"}
