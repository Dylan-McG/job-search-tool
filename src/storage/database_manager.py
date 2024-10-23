from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import logging

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(String, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    salary = Column(Float)
    description = Column(Text)
    url = Column(String)
    score = Column(Float)

class DatabaseManager:
    def __init__(self, db_config):
        self.engine = create_engine(db_config['connection_string'])
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.logger = logging.getLogger(__name__)

    def save_jobs(self, jobs):
        session = self.Session()
        try:
            for job in jobs:
                job_entry = Job(
                    id=job.get('id') or job.get('url'),
                    title=job.get('title'),
                    company=job.get('company', {}).get('display_name'),
                    location=job.get('location', {}).get('display_name'),
                    salary=job.get('salary'),
                    description=job.get('description'),
                    url=job.get('redirect_url'),
                    score=job.get('score')
                )
                session.merge(job_entry)
            session.commit()
            self.logger.info(f"Saved {len(jobs)} jobs to the database.")
        except Exception as e:
            session.rollback()
            self.logger.error(f"Error saving jobs to database: {e}")
        finally:
            session.close()
