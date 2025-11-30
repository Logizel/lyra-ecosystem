from fastapi import FastAPI
from .socket.server import socket_app

app = FastAPI(title="Lyra Core")

app.mount("/", socket_app)

@app.get("/health")
async def health_check():
    return {"status": "Lyra is awake"}
