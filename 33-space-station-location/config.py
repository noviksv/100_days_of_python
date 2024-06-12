import smtplib
import logging
from dotenv import load_dotenv
import os
import smtplib
import logging
import random
import datetime as dt

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_LOGIN = os.getenv("SMTP_LOGIN")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM = os.getenv("SMTP_FROM")

def send_email(message_subject, message_body):
    with smtplib.SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=SMTP_LOGIN, password=SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_FROM,
            to_addrs=SMTP_FROM,
            msg=f"Subject:{message_subject}\n\n{message_body}"
        )
        logging.info("Email sent")
