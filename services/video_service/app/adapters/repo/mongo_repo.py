from app.domain.models import Video, VideoStatus
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId


class MongoVideoRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["videos"]

    async def create_video(self, video: Video) -> str:
        data = video.dict(exclude={"id"})
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def list_videos(self):
        cursor = self.collection.find()
        return [Video(**v, id=str(v["_id"])) async for v in cursor]

    async def update_status(self, video_id: str, status: VideoStatus):
        await self.collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": {"status": status.value}}
        )
    async def delete_video(self, video_id: str):
        await self.collection.delete_one({"_id": ObjectId(video_id)})


