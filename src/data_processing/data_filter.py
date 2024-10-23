class DataFilter:
    def __init__(self, criteria):
        self.salary_min = criteria.get('salary_min', 0)
        self.salary_max = criteria.get('salary_max', float('inf'))
        self.exclude_keywords = criteria.get('exclude_keywords', [])
    
    def filter_jobs(self, jobs):
        filtered_jobs = []
        for job in jobs:
            if self._is_valid(job):
                filtered_jobs.append(job)
        return filtered_jobs
    
    def _is_valid(self, job):
        salary = job.get('salary', 0)
        if not (self.salary_min <= salary <= self.salary_max):
            return False
        job_title = job.get('title', '').lower()
        for keyword in self.exclude_keywords:
            if keyword.lower() in job_title:
                return False
        return True
