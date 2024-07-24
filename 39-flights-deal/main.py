import os
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv

from data_manager import DataManager
from flight_search import FlightSearch
from twilio_sms import send_message

load_dotenv()

ORIGIN_LOCATION_CODE = os.getenv('ORIGIN_LOCATION_CODE', 'WAW')
DAYS_TO_SEARCH = int(os.getenv('DAYS_TO_SEARCH', 2))
ADULTS = int(os.getenv('ADULTS', 1))
MAX_RESULTS = int(os.getenv('MAX_RESULTS', 10))

logging.basicConfig(level=logging.INFO)

def find_cheapest_flight(flight_search, destination, max_price):
    tomorrow = datetime.now().date() + timedelta(days=1)
    for days_offset in range(DAYS_TO_SEARCH):
        current_date = tomorrow + timedelta(days=days_offset)
        flight_offers = flight_search.search_flight_offers(
            ORIGIN_LOCATION_CODE,
            destination['iataCode'],
            current_date,
            ADULTS,
            MAX_RESULTS
        )

        if flight_offers['meta']['count'] > 0:
            for flight_offer in flight_offers['data']:
                price = float(flight_offer['price']['grandTotal'])
                currency = flight_offer['price']['currency']
                if price < max_price:
                    message = f"Price is low: {price} {currency} for {destination['iataCode']} {current_date}"
                    send_message(
                        account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
                        auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
                        from_=os.getenv("TWILIO_FROM"),
                        to=os.getenv("TWILIO_TO"),
                        message_body=message
                    )
                    logging.info(message)
                    return
        else:
            logging.debug(f"No flight offers found for {destination['iataCode']} on {current_date}")

    logging.info(f"No suitable flights found for {destination['iataCode']} from {tomorrow} to {current_date}")

if __name__ == "__main__":
    data_manager = DataManager()
    flight_search = FlightSearch()

    sheet_data = data_manager.get_sheet_data()
    if not all(destination['iataCode'] for destination in sheet_data):
        for destination in sheet_data:
            if not destination['iataCode']:
                destination['iataCode'] = flight_search.search_iata_by_city_name(destination['city'])
        data_manager.update_destination_codes()

    for destination in sheet_data:
        find_cheapest_flight(flight_search, destination, destination['lowestPrice'])
