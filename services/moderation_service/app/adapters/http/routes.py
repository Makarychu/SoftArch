from fastapi import APIRouter, HTTPException
from ...domain.models import ModerationRequest, ModerationStatus
from ..repo.memory_repo import InMemoryModerationRepo
from ...infrastructure.clients import update_video_status

repo = InMemoryModerationRepo()
router = APIRouter()

@router.post("/moderations")
async def create_request(data: dict):
    req = ModerationRequest.create(video_id=data["video_id"])
    await repo.add_request(req)
    return req

@router.get("/moderations")
async def list_requests():
    return await repo.list_requests()

@router.get("/moderations/{req_id}")
async def get_request(req_id: str):
    req = await repo.get_request(req_id)
    if not req:
        raise HTTPException(404)
    return req

@router.patch("/moderations/{req_id}")
async def update_request(req_id: str, data: dict):
    req = await repo.update_request(req_id, **data)
    if not req:
        raise HTTPException(404)
    if req.status == ModerationStatus.APPROVED:
        await update_video_status(req.video_id, "PUBLISHED")
    elif req.status == ModerationStatus.REJECTED:
        await update_video_status(req.video_id, "REJECTED")
    return req

@router.delete("/moderations/{req_id}")
async def delete_request(req_id: str):
    deleted = await repo.delete_request(req_id)
    if not deleted:
        raise HTTPException(404)
    return {"deleted": req_id}

@router.get("/health/db")
async def health_db():
    try:
        await db.command("ping")
        return {"status": "ok", "db": "reachable"}
    except Exception as e:
        return {"status": "error", "db": "unreachable", "detail": str(e)}