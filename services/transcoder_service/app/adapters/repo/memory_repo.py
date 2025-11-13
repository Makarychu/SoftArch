from typing import Dict
from ...domain.models import TranscodeJob

class InMemoryTranscodeRepo:
    def __init__(self):
        self.jobs: Dict[str, TranscodeJob] = {}

    async def add_job(self, job: TranscodeJob):
        self.jobs[job.id] = job
        return job

    async def get_job(self, job_id: str):
        return self.jobs.get(job_id)

    async def list_jobs(self):
        return list(self.jobs.values())

    async def update_job(self, job_id: str, **updates):
        job = self.jobs.get(job_id)
        if not job:
            return None
        for key, value in updates.items():
            setattr(job, key, value)
        return job

    async def delete_job(self, job_id: str):
        return self.jobs.pop(job_id, None)
