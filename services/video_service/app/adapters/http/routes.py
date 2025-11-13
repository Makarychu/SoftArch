from fastapi import APIRouter, Depends
from app.infrastructure.db import get_db
from app.adapters.repo.mongo_repo import MongoVideoRepository
from app.usecase.video_service import VideoService
from fastapi import Depends
from app.core.auth import verify_token

router = APIRouter()


@router.post("/videos/upload-session")
async def create_upload_session(data: dict, db=Depends(get_db)):
    repo = MongoVideoRepository(db)
    service = VideoService(repo)
    return await service.create_upload_session(data)


@router.post("/videos/transcode/callback")
async def handle_transcode_callback(payload: dict, db=Depends(get_db)):
    repo = MongoVideoRepository(db)
    service = VideoService(repo)
    video_id = payload.get("video_id")
    success = payload.get("success", True)
    return await service.handle_transcode_callback(video_id, success)


@router.patch("/videos/{video_id}/status")
async def change_status(video_id: str, payload: dict, db=Depends(get_db)):
    repo = MongoVideoRepository(db)
    service = VideoService(repo)
    new_status = payload.get("status")
    return await service.change_moderation_status(video_id, new_status)


@router.get("/videos")
async def list_videos(db=Depends(get_db)):
    repo = MongoVideoRepository(db)
    service = VideoService(repo)
    return await service.list_videos()

@router.delete("/videos/{video_id}")
async def delete_video(video_id: str, db=Depends(get_db)):
    repo = MongoVideoRepository(db)
    await repo.delete_video(video_id)
    return {"deleted": video_id}

@router.post("/upload")
def upload_video(..., user_id = Depends(get_current_user)
):
    return {"msg": f"Video uploaded by {user['username']}"}



