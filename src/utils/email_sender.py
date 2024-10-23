import smtplib
import logging
from email.message import EmailMessage

class EmailSender:
    def __init__(self, email_config):
        self.smtp_server = email_config['smtp_server']
        self.smtp_port = email_config['smtp_port']
        self.username = email_config['username']
        self.password = email_config['password']
        self.recipient = email_config['recipient']
        self.logger = logging.getLogger(__name__)

    def send_email(self, attachment_path):
        msg = EmailMessage()
        msg['Subject'] = 'Daily Job Report'
        msg['From'] = self.username
        msg['To'] = self.recipient
        msg.set_content('Please find the attached job report.')

        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)
            self.logger.info("Email sent successfully.")
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")
