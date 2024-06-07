import smtplib
import logging
from dotenv import load_dotenv
import os
import smtplib
import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_LOGIN = os.getenv("SMTP_LOGIN")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM = os.getenv("SMTP_FROM")

with smtplib.SMTP(SMTP_HOST) as connection:
    connection.starttls()
    connection.login(user=SMTP_LOGIN, password=SMTP_PASSWORD)
    connection.sendmail(
        from_addr=SMTP_FROM,
        to_addrs=SMTP_FROM,
        msg="Subject:Hello\n\nThis is the body of my email"
    )
    logging.info("Email sent")