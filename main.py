import logging
from config.settings import load_config
from src.utils.logger import setup_logging
from src.api_clients.adzuna_client import AdzunaClient
from src.api_clients.jooble_client import JoobleClient
from src.data_processing.data_aggregator import DataAggregator
from src.data_processing.data_filter import DataFilter
from src.data_processing.deduplicator import Deduplicator
from src.ranking.ranking_engine import RankingEngine
from src.storage.database_manager import DatabaseManager
from src.reporting.report_generator import ReportGenerator
from src.utils.email_sender import EmailSender

def main():
    # Load configuration
    config = load_config()
    
    # Setup logging
    setup_logging(config['logging'])
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Job Search Tool started.")

        # Instantiate API clients
        adzuna_client = AdzunaClient(config['api_keys']['adzuna'])
        jooble_client = JoobleClient(config['api_keys']['jooble'])
        
        # Fetch job listings
        adzuna_jobs = adzuna_client.search_jobs(config['job_search'])
        jooble_jobs = jooble_client.search_jobs(config['job_search'])
        
        # Aggregate data
        aggregator = DataAggregator()
        all_jobs = aggregator.aggregate([adzuna_jobs, jooble_jobs])
        
        # Process data
        filterer = DataFilter(config['filter_criteria'])
        filtered_jobs = filterer.filter_jobs(all_jobs)
        
        deduplicator = Deduplicator()
        unique_jobs = deduplicator.remove_duplicates(filtered_jobs)
        
        # Rank jobs
        ranker = RankingEngine(config['ranking'])
        ranked_jobs = ranker.rank_jobs(unique_jobs)
        
        # Store in database
        db_manager = DatabaseManager(config['database'])
        db_manager.save_jobs(ranked_jobs)
        
        # Generate report
        report_generator = ReportGenerator(config['report'])
        report_file = report_generator.generate(ranked_jobs)
        
        # Send email
        email_sender = EmailSender(config['email'])
        email_sender.send_email(report_file)
        
        logger.info("Job Search Tool completed successfully.")
    except Exception as e:
        logger.exception("An error occurred during execution.")
        raise e

if __name__ == "__main__":
    main()
