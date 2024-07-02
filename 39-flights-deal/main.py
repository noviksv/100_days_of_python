#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
import os
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch


load_dotenv()




my_destinations = DataManager()
sheet_data = my_destinations.get_sheet_data()
pprint(sheet_data)
if sheet_data[0]["iataCode"] == "":
    for destination in sheet_data:
        destination["iataCode"] = FlightSearch(destination["city"]).search()
        #my_destinations.update_destination_codes(destination)
    my_destinations.destination_data = sheet_data
    my_destinations.update_destination_codes()
    
#pprint(sheet_data)
