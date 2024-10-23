import spacy
import logging

class RankingEngine:
    def __init__(self, ranking_config):
        self.weights = ranking_config.get('weights', {'relevance': 0.7, 'salary': 0.3})
        self.nlp = spacy.load('en_core_web_sm')
        self.logger = logging.getLogger(__name__)

    def rank_jobs(self, jobs):
        for job in jobs:
            job['score'] = self._calculate_score(job)
        ranked_jobs = sorted(jobs, key=lambda x: x['score'], reverse=True)
        self.logger.info("Jobs have been ranked.")
        return ranked_jobs

    def _calculate_score(self, job):
        relevance_score = self._calculate_relevance(job)
        salary_score = self._normalize_salary(job.get('salary', 0))
        total_score = (self.weights['relevance'] * relevance_score) + (self.weights['salary'] * salary_score)
        return total_score

    def _calculate_relevance(self, job):
        keywords = job.get('title', '') + ' ' + job.get('description', '')
        doc = self.nlp(keywords)
        # Simple example: count the number of times keywords appear
        return len([token for token in doc if token.text.lower() in ['python', 'developer']])

    def _normalize_salary(self, salary):
        max_salary = 200000  # Adjust based on expected maximum
        return salary / max_salary
