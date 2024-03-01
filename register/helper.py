import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time

class SendMail:
    def send_email(self, sender_email, receiver_emails, subject, body, password):
        try:
            # Create a multipart message
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_emails
            message['Subject'] = subject

            # Attach the body to the email
            message.attach(MIMEText(body, 'plain'))

            # Create an SMTP session
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.starttls()
            smtpObj.login(sender_email, password)

            # Send the email
            smtpObj.sendmail(sender_email, receiver_emails, message.as_string())

            print("Successfully sent email")
        except Exception as e:
            print("Error:", e)
