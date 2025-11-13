import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DB_NAME")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
