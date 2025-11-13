import httpx, os

VIDEO_SERVICE_URL = os.getenv("VIDEO_SERVICE_URL", "http://video-service:8000")

async def update_video_status(video_id: str, status: str):
    async with httpx.AsyncClient() as client:
        await client.patch(f"{VIDEO_SERVICE_URL}/videos/{video_id}/status",
                           json={"status": status})
