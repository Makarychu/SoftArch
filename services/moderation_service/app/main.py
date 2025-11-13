from fastapi import FastAPI
from pydantic import BaseModel
import httpx, os

app = FastAPI(title="Moderation Service")

VIDEO_SERVICE_URL = os.getenv("VIDEO_SERVICE_URL", "http://video-service:8000")

class ModerationRequest(BaseModel):
    video_id: str
    approved: bool = True

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/moderate")
async def moderate_video(data: ModerationRequest):
    status = "APPROVED" if data.approved else "REJECTED"

    async with httpx.AsyncClient() as client:
        await client.patch(f"{VIDEO_SERVICE_URL}/videos/{data.video_id}/status",
                           json={"status": status})
    return {"video_id": data.video_id, "status": status}
