import requests
# from requests.auth 
from dotenv import load_dotenv
import os

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._endpoint = os.getenv("SHEETY_ENDPOINT")
        self._headers = {
        "Authorization": f"Bearer {os.getenv('SHEETY_BEARER')}"
    }
        self.destination_data = {}

    def get_destinations(self):
        #Returns a list of dictionaries representing the destinations.
        pass

    def get_sheet_data(self)    :
        #Returns a list of dictionaries representing the data in the sheet.
        # headers = {
        #     "Authorization": f"Bearer {os.getenv('SHEETY_BEARER')}"
        # }
        r = requests.get(url=self._endpoint, headers=self._headers)
        r.raise_for_status()
        self.destination_data = r.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        #Updates the destination codes in the sheet.
        for city in self.destination_data:
            updated_data ={"price" : {"iataCode" : city["iataCode"] }}
            r = requests.put(url=f"{self._endpoint}/{city['id']}", headers=self._headers
                            , json=updated_data )
            r.raise_for_status()
            print(r.text)