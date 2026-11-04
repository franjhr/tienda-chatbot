from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes.chat import router as chat_router

WEB_DIR = Path(__file__).resolve().parent.parent / "web"

app = FastAPI(title="Chatbot de la tienda")

app.include_router(chat_router)

app.mount("/", StaticFiles(directory=WEB_DIR, html=True), name="web")
