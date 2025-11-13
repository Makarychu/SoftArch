from typing import Dict
from ...domain.models import ModerationRequest

class InMemoryModerationRepo:
    def __init__(self):
        self.data: Dict[str, ModerationRequest] = {}

    async def add_request(self, req: ModerationRequest):
        self.data[req.id] = req
        return req

    async def get_request(self, req_id: str):
        return self.data.get(req_id)

    async def list_requests(self):
        return list(self.data.values())

    async def update_request(self, req_id: str, **updates):
        req = self.data.get(req_id)
        if not req:
            return None
        for k, v in updates.items():
            setattr(req, k, v)
        return req

    async def delete_request(self, req_id: str):
        return self.data.pop(req_id, None)
