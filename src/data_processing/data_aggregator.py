class DataAggregator:
    def aggregate(self, job_lists):
        aggregated_jobs = []
        for jobs in job_lists:
            aggregated_jobs.extend(jobs)
        return aggregated_jobs
