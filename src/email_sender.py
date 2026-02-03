import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL_NAME = os.environ.get("SENDER_EMAIL_NAME")
SENDER_EMAIL_ADDRESS = os.environ.get("SENDER_EMAIL_ADDRESS")
SENDER_EMAIL_PASSWORD = os.environ.get("SENDER_EMAIL_PASSWORD")

def send_email(subject, html_body, to_addresses):
    if not SENDER_EMAIL_ADDRESS or not SENDER_EMAIL_PASSWORD:
        print("Missing SENDER_EMAIL_ADDRESS or SENDER_EMAIL_PASSWORD in .env")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{SENDER_EMAIL_NAME} <{SENDER_EMAIL_ADDRESS}>"
    msg["To"] = ", ".join(to_addresses)

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
        smtp.sendmail(SENDER_EMAIL_ADDRESS, to_addresses, msg.as_string())

    print("Email sent!")
