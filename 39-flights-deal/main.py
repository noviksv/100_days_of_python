#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
import os
from pprint import pprint
from datetime import datetime, timedelta
import time

from data_manager import DataManager
from flight_search import FlightSearch
from twilio_sms import send_message


load_dotenv()

my_destinations = DataManager()
sheet_data = my_destinations.get_sheet_data()
pprint(sheet_data)
fl = FlightSearch()

#updating IATA codes for airports
if sheet_data[0]["iataCode"] == "":
    for destination in sheet_data:
        destination["iataCode"] = fl.search_iata_by_city_name(destination["city"])
    my_destinations.destination_data = sheet_data
    my_destinations.update_destination_codes()
    


# Get tomorrow's date
tomorrow = datetime.now().date() + timedelta(days=1)
origin_location_code='WAW'
destination_location_code='NYC'
adults=1
max_results=10
max_price=1000

# Iterate over the next 180 days




for day in range((tomorrow + timedelta(days=2) - tomorrow).days):
    current_date = tomorrow + timedelta(days=day)
    departure_date=current_date
    fo = fl.search_flight_offers(origin_location_code, destination_location_code, departure_date, adults, max_results)

    #iterate every day from tomorrow to +180 days

    #try:
    while 1 == 1:
        if fo["meta"]["count"] > 0:
            print("Flight offers found:")
            for flight_offer in fo['data']:
                # print(flight_offer['itineraries'][0]['segments'][0]['departure']['iataCode'],'-->'
                #     ,flight_offer['itineraries'][0]['segments'][0]['arrival']['iataCode'])
                price = float(flight_offer['price']["grandTotal"])
                currency = flight_offer['price']["currency"]
                print(price)
                if price < max_price:
                    msg = f"Price is low: {price} {currency} for {destination_location_code} {current_date}"
                    send_message(account_sid=os.getenv("TWILIO_ACCOUNT_SID"), auth_token=os.getenv("TWILIO_AUTH_TOKEN")
                    , from_=os.getenv("TWILIO_FROM"), to=os.getenv("TWILIO_TO"), message_body=msg)
                    print(msg)
                    # exit from the outer for loop
                    break
            # exit from the outer for loop
            break


        else:
            print("No flight offers found.")
    # except:
    #     print("skipping ",current_date )
    time.sleep(0.5)



## TODO:
# refactor logic, loops
# print --> logging
