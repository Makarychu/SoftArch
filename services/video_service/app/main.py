from fastapi import FastAPI, Depends
from .adapters.http.routes import router
from app.core.auth import verify_token

app = FastAPI(
    title="Video Service",
    root_path="/video"   # для video-service
)

app.include_router(router, prefix="/api")










