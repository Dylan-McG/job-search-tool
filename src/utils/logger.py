import logging
import os

def setup_logging(logging_config):
    log_level = logging_config.get('level', 'INFO')
    log_file = logging_config.get('log_file', 'logs/app.log')
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=getattr(logging, log_level.upper(), logging.INFO),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
