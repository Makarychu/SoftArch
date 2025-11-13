from pydantic import BaseModel
from enum import Enum
from typing import Optional
import uuid

class JobStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    DONE = "DONE"
    FAILED = "FAILED"

class TranscodeJob(BaseModel):
    id: str
    video_id: str
    status: JobStatus = JobStatus.PENDING
    output_url: Optional[str] = None

    @classmethod
    def create(cls, video_id: str):
        return cls(id=str(uuid.uuid4()), video_id=video_id)
