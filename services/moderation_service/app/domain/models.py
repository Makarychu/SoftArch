from pydantic import BaseModel
from enum import Enum
from typing import Optional
import uuid

class ModerationStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class ModerationRequest(BaseModel):
    id: str
    video_id: str
    status: ModerationStatus = ModerationStatus.PENDING
    reason: Optional[str] = None

    @classmethod
    def create(cls, video_id: str):
        return cls(id=str(uuid.uuid4()), video_id=video_id)
