import requests
import logging

class AdzunaClient:
    def __init__(self, credentials):
        self.app_id = credentials['app_id']
        self.app_key = credentials['app_key']
        self.base_url = "https://api.adzuna.com/v1/api/jobs"
        self.logger = logging.getLogger(__name__)

    def search_jobs(self, search_params):
        url = f"{self.base_url}/{search_params['country_code']}/search/1"
        params = {
            'app_id': self.app_id,
            'app_key': self.app_key,
            'what': search_params['keywords'],
            'where': search_params['location'],
            'results_per_page': 50,
            'content-type': 'application/json'
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            jobs = response.json().get('results', [])
            self.logger.info(f"Fetched {len(jobs)} jobs from Adzuna.")
            return jobs
        except requests.RequestException as e:
            self.logger.error(f"Error fetching jobs from Adzuna: {e}")
            return []
