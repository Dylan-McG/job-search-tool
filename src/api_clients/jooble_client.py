import requests
import logging

class JoobleClient:
    def __init__(self, credentials):
        self.api_key = credentials['api_key']
        self.base_url = "https://jooble.org/api/"
        self.logger = logging.getLogger(__name__)

    def search_jobs(self, search_params):
        url = f"{self.base_url}{self.api_key}"
        payload = {
            'keywords': search_params['keywords'],
            'location': search_params['location'],
            'page': 1
        }
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            jobs = response.json().get('jobs', [])
            self.logger.info(f"Fetched {len(jobs)} jobs from Jooble.")
            return jobs
        except requests.RequestException as e:
            self.logger.error(f"Error fetching jobs from Jooble: {e}")
            return []
