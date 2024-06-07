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

def send_email(message_body):
    with smtplib.SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=SMTP_LOGIN, password=SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_FROM,
            to_addrs=SMTP_FROM,
            msg=f"Subject:Hello\n\n{message_body}"
        )
        logging.info("Email sent")

def get_random_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
    quote = random.choice(quotes)
    logging.info(f"Selected quote: {quote}")
    return quote

def main():
    if dt.datetime.now().weekday() == 4:
        logging.info("It's Friday! Sending email.")
        send_email(get_random_quote())
    else:
        logging.info("It's not Friday. No email sent.")


if __name__ == "__main__":
    main()