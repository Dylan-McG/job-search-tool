import unittest
from src.api_clients.adzuna_client import AdzunaClient

class TestAdzunaClient(unittest.TestCase):
    def setUp(self):
        credentials = {
            'app_id': 'test_app_id',
            'app_key': 'test_app_key'
        }
        self.client = AdzunaClient(credentials)

    def test_search_jobs(self):
        search_params = {
            'country_code': 'gb',
            'keywords': 'Python Developer',
            'location': 'London'
        }
        jobs = self.client.search_jobs(search_params)
        self.assertIsInstance(jobs, list)

if __name__ == '__main__':
    unittest.main()
