class Deduplicator:
    def remove_duplicates(self, jobs):
        unique_jobs = []
        seen = set()
        for job in jobs:
            job_id = job.get('id') or job.get('url')
            if job_id and job_id not in seen:
                seen.add(job_id)
                unique_jobs.append(job)
        return unique_jobs
