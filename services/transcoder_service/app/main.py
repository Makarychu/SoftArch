from fastapi import FastAPI
from .adapters.http.routes import router

app = FastAPI(
    title="Transcoder Service",
    root_path="/transcoder"   # для video-service
)
app.include_router(router, prefix="/api")
