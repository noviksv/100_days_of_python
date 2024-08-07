from dotenv import load_dotenv
import os
import requests

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        #self.destination_city = destination_city
        self.access_token = None
        self.get_access_token()
        pass
    
    def search(self):
        return "TEST"
    

    def get_access_token(self):
        load_dotenv()
        api_key = os.getenv('AMADEUS_API_KEY') 
        api_secret = os.getenv('AMADEUS_API_SECRET')
        url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'grant_type': 'client_credentials',
            'client_id': api_key,
            'client_secret': api_secret
        }


        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            print('Access token obtained successfully!')
            access_token = response.json().get('access_token')
            # print(f'Access token: {access_token}')
            self.access_token = access_token
        else:
            print(f'Failed to obtain access token. Status code: {response.status_code}')
            print(response.text)
            return None
    


    def search_iata_by_city_name(self, city_name):
        url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        params = {
            "keyword": city_name
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            try:
                iata_code = response.json().get('data')[0].get('iataCode')
                print(f'IATA code for {city_name}: {iata_code}')
            except IndexError:
                print(f"IndexError: No airport code found for {city_name}.")
                return "N/A"
            except (KeyError, TypeError):
                print(f"KeyError or TypeError: No airport code found for {city_name}.")
                return "Not Found"
            
            return iata_code
        else:
            print(f'Failed to obtain IATA code. Status code: {response.status_code}')
            print(response.text)

    def search_flight_offers(self, origin_location_code, destination_location_code, departure_date, adults, max_results):
        url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

        params = {
            "originLocationCode": origin_location_code,
            "destinationLocationCode": destination_location_code,
            "departureDate": departure_date,
            "adults": adults,
            "max": max_results,
            "nonStop": "true"
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return(response.json())
        else:
            print(f'Failed to obtain flight offers. Status code: {response.status_code}')
            return(response.json())
