import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI
from api.auth import router as auth_router

app = FastAPI(title="Lyra API", version="0.1.0")

app.include_router(auth_router, prefix="/api")


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
