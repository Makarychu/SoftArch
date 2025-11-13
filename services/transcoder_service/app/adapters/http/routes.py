from fastapi import APIRouter, HTTPException
from ...domain.models import TranscodeJob, JobStatus
from ..repo.memory_repo import InMemoryTranscodeRepo
from ...infrastructure.clients import notify_video_service

repo = InMemoryTranscodeRepo()
router = APIRouter()

@router.post("/jobs")
async def create_job(data: dict):
    job = TranscodeJob.create(video_id=data["video_id"])
    await repo.add_job(job)
    return job

@router.get("/jobs")
async def list_jobs():
    return await repo.list_jobs()

@router.get("/jobs/{job_id}")
async def get_job(job_id: str):
    job = await repo.get_job(job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job

@router.patch("/jobs/{job_id}")
async def update_job(job_id: str, data: dict):
    job = await repo.update_job(job_id, **data)
    if not job:
        raise HTTPException(404)
    if job.status == JobStatus.DONE:
        await notify_video_service(job.video_id, True)
    elif job.status == JobStatus.FAILED:
        await notify_video_service(job.video_id, False)
    return job

@router.delete("/jobs/{job_id}")
async def delete_job(job_id: str):
    deleted = await repo.delete_job(job_id)
    if not deleted:
        raise HTTPException(404)
    return {"deleted": job_id}

@router.get("/health-db")
async def health_db():
    try:
        await db.command("ping")
        return {"status": "ok", "db": "reachable"}
    except Exception as e:
        return {"status": "error", "db": "unreachable", "detail": str(e)}
