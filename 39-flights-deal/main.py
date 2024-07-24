#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
import os
from pprint import pprint
from datetime import datetime, timedelta
import time
import logging

from data_manager import DataManager
from flight_search import FlightSearch
from twilio_sms import send_message

logging.basicConfig(level=logging.INFO)

load_dotenv()

ORIGIN_LOCATION_CODE='WAW'
DAYS = 2



def find_cheapest_flight(days_,origin_location_code,destination_location_code, max_price):
    for day in range((tomorrow + timedelta(days=days_) - tomorrow).days):
        current_date = tomorrow + timedelta(days=day)
        departure_date=current_date
        fo = fl.search_flight_offers(origin_location_code, destination_location_code, departure_date, adults, max_results)

        #iterate every day from tomorrow to +180 days

        try:
        #while 1 == 1:
            if fo["meta"]["count"] > 0:
                logging.debug("Flight offers found:")
                for flight_offer in fo['data']:
                    # logging.debug(flight_offer['itineraries'][0]['segments'][0]['departure']['iataCode'],'-->'
                    #     ,flight_offer['itineraries'][0]['segments'][0]['arrival']['iataCode'])
                    price = float(flight_offer['price']["grandTotal"])
                    currency = flight_offer['price']["currency"]
                    logging.debug((price,currency))
                    if price < max_price:
                        msg = f"Price is low: {price} {currency} for {destination_location_code} {current_date}"
                        send_message(account_sid=os.getenv("TWILIO_ACCOUNT_SID"), auth_token=os.getenv("TWILIO_AUTH_TOKEN")
                        , from_=os.getenv("TWILIO_FROM"), to=os.getenv("TWILIO_TO"), message_body=msg)
                        logging.info(msg)
                        return



            else:
                logging.debug(f"No flight offers found for date {current_date}")
        except:
            logging.debug("error occured, skipping ",current_date )
        time.sleep(0.5)
    logging.info(f"No suitable flights found for {destination_location_code} {tomorrow}...{current_date}")
    return




if __name__ == "__main__":

    my_destinations = DataManager()
    sheet_data = my_destinations.get_sheet_data()
    #pprint(sheet_data)
    fl = FlightSearch()


    #updating IATA codes for airports
    if sheet_data[0]["iataCode"] == "":
        for destination in sheet_data:
            destination["iataCode"] = fl.search_iata_by_city_name(destination["city"])
        my_destinations.destination_data = sheet_data
        my_destinations.update_destination_codes()
        

    # go through destinations
    for destination in sheet_data:
        destination_location_code= destination["iataCode"]
        max_price= destination["lowestPrice"]
        logging.info(f"Destination is {destination_location_code}, price is {max_price}")
        tomorrow = datetime.now().date() + timedelta(days=1)
        adults=1
        max_results=10

        find_cheapest_flight(days_=DAYS, origin_location_code=ORIGIN_LOCATION_CODE, destination_location_code=destination_location_code,  max_price=max_price)
