import httpx
import os

VIDEO_SERVICE_URL = os.getenv("VIDEO_SERVICE_URL", "http://video-service:8000")

async def notify_video_service(video_id: str, success: bool):
    async with httpx.AsyncClient() as client:
        await client.post(f"{VIDEO_SERVICE_URL}/videos/transcode/callback",
                          json={"video_id": video_id, "success": success})
