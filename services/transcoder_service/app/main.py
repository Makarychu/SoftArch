from fastapi import FastAPI
from .adapters.http.routes import router

app = FastAPI(title="Transcoder Service")
app.include_router(router, prefix="/api")
