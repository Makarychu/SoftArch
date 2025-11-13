from fastapi import FastAPI, Depends
from app.core.auth import verify_token
from app.adapters.http.routes import router

app = FastAPI(title="Video Service")
app.include_router(router, prefix="/api")



