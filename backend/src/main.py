import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI, Depends
from api.auth import router as auth_router, get_current_user  # Import the dependency

app = FastAPI(title="Lyra API", version="0.1.0")

app.include_router(auth_router, prefix="/api")


@app.get("/health")
def health_check():
    """Public health check - no token needed."""
    return {"status": "ok"}


@app.get("/health/protected", dependencies=[Depends(get_current_user)])
def health_check_protected():
    """Protected health check - requires valid token."""
    return {"status": "ok", "message": "You have a valid token!"}
