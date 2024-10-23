import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    config = {
        'api_keys': {
            'adzuna': {
                'app_id': os.getenv('ADZUNA_APP_ID'),
                'app_key': os.getenv('ADZUNA_APP_KEY')
            },
            'jooble': {
                'api_key': os.getenv('JOOBLE_API_KEY')
            }
        },
        'job_search': {
            'keywords': os.getenv('JOB_KEYWORDS', 'Python Developer'),
            'location': os.getenv('JOB_LOCATION', 'London'),
            'country_code': os.getenv('COUNTRY_CODE', 'gb')
        },
        'filter_criteria': {
            'salary_min': int(os.getenv('SALARY_MIN', 50000)),
            'salary_max': int(os.getenv('SALARY_MAX', 150000)),
            'exclude_keywords': os.getenv('EXCLUDE_KEYWORDS', '').split(',')
        },
        'ranking': {
            'weights': {
                'relevance': 0.7,
                'salary': 0.3
            }
        },
        'database': {
            'connection_string': os.getenv('DATABASE_URL', 'sqlite:///data/jobs.db')
        },
        'report': {
            'output_dir': os.getenv('REPORT_OUTPUT_DIR', 'data/reports')
        },
        'email': {
            'smtp_server': os.getenv('EMAIL_SMTP_SERVER'),
            'smtp_port': int(os.getenv('EMAIL_SMTP_PORT', 587)),
            'username': os.getenv('EMAIL_USERNAME'),
            'password': os.getenv('EMAIL_PASSWORD'),
            'recipient': os.getenv('EMAIL_RECIPIENT')
        },
        'logging': {
            'level': os.getenv('LOG_LEVEL', 'INFO'),
            'log_file': os.getenv('LOG_FILE', 'logs/app.log')
        }
    }
    return config
