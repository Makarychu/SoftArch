from fastapi import FastAPI
from .adapters.http.routes import router

app = FastAPI(
    title="Moderation Service",
    root_path="/moderation"   # для video-service
)
app.include_router(router, prefix="/api")
