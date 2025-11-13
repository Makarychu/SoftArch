from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VideoStatus(str, Enum):
    DRAFT = "DRAFT"
    PENDING = "PENDING_MODERATION"
    PUBLISHED = "PUBLISHED"
    REJECTED = "REJECTED"


class Video(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    author: str
    status: VideoStatus = VideoStatus.DRAFT
    created_at: datetime = Field(default_factory=datetime.utcnow)
