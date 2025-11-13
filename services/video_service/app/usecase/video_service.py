from app.domain.models import Video, VideoStatus
from app.adapters.repo.mongo_repo import MongoVideoRepository


class VideoService:
    def __init__(self, repo: MongoVideoRepository):
        self.repo = repo

    async def create_upload_session(self, data: dict) -> dict:
        video = Video(**data)
        vid = await self.repo.create_video(video)
        return {"upload_url": f"https://fake-s3.local/{vid}", "id": vid}

    async def handle_transcode_callback(self, video_id: str, success: bool):
        new_status = VideoStatus.PUBLISHED if success else VideoStatus.PENDING
        await self.repo.update_status(video_id, new_status)
        return {"status": new_status}

    async def change_moderation_status(self, video_id: str, status: str):
        await self.repo.update_status(video_id, VideoStatus(status))
        return {"status": status}

    async def list_videos(self):
        return await self.repo.list_videos()
