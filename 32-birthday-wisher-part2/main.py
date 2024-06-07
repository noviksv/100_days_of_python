##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

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

def get_birthdays():
    with open("birthdays.csv") as file:
        birthdays = file.readlines()
    return birthdays


def main():
    for birthday in get_birthdays():
        if dt.datetime.now().strftime("%m-%d") == f"{birthday.split(',')[3].strip()}-{birthday.split(',')[4].strip()}":
            logging.info("It's someone's birthday! Sending email.")
            name = birthday.split(',')[0]
            with open(f"letter_templates/letter_{random.choice(range(1,3))}.txt") as file:
                letter = file.read()
                letter = letter.replace("[NAME]", name)
                logging.info(f"Letter: {letter}")
                send_email(letter)
        else:
            logging.info("It's not someone's birthday. No email sent.")


if __name__ == "__main__":
    main()


