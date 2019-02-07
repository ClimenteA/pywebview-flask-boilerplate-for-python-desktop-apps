import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:
    
    """Sending an email with smtp library"""

    def __init__(self, smtpaddr, smtpport):
        self.smtpaddr = smtpaddr
        self.smtpport = smtpport

    def check_mail_inputs(self, fromaddr, frompassword, toaddr, subject, body):
        """All must be type string"""
        inputs_mail = [fromaddr, frompassword, toaddr, subject, body]
        
        for i in inputs_mail:
            if not isinstance(i, str):
                raise Exception("Parameter must be string!")
            
            
    def send_mail(self, fromaddr, frompassword, toaddr, subject, body):
        """Send  and email using standard smtp module"""
        self.check_mail_inputs(fromaddr, frompassword, toaddr, subject, body)
        
        msg = MIMEMultipart()
        
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.smtpaddr, self.smtpport)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, frompassword)

        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)