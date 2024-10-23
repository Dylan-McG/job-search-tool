from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
import logging
from datetime import datetime

class ReportGenerator:
    def __init__(self, report_config):
        self.output_dir = report_config['output_dir']
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def generate(self, jobs):
        filename = os.path.join(self.output_dir, f"job_report_{datetime.now().strftime('%Y%m%d')}.pdf")
        doc = SimpleDocTemplate(filename)
        styles = getSampleStyleSheet()
        flowables = []
        for job in jobs:
            title = Paragraph(f"<b>{job['title']}</b>", styles['Title'])
            company = Paragraph(f"Company: {job.get('company', {}).get('display_name', 'N/A')}", styles['Normal'])
            location = Paragraph(f"Location: {job.get('location', {}).get('display_name', 'N/A')}", styles['Normal'])
            salary = Paragraph(f"Salary: {job.get('salary', 'N/A')}", styles['Normal'])
            description = Paragraph(job.get('description', ''), styles['BodyText'])
            spacer = Spacer(1, 12)
            flowables.extend([title, company, location, salary, description, spacer])
        doc.build(flowables)
        self.logger.info(f"Report generated at {filename}.")
        return filename
