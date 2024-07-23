import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
import time
import json


load_dotenv() # take environment variables from .env.
#working with amadeus api


def get_access_token():
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
        return access_token
    else:
        print(f'Failed to obtain access token. Status code: {response.status_code}')
        print(response.text)
        return None
    

access_token = get_access_token()

#access_token = 'H8ZvqWOCaH7VA6B7kJVPmEqAIULs'

def search_iata_by_city_name(access_token, city_name):
    url = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    params = {
        "keyword": city_name
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        iata_code = response.json().get('data')[0].get('iataCode')
        print(f'IATA code for {city_name}: {iata_code}')
        return iata_code
    else:
        print(f'Failed to obtain IATA code. Status code: {response.status_code}')
        print(response.text)


# search_iata_by_city_name(access_token, 'Warsaw')

def search_flight_offers(access_token, origin_location_code, destination_location_code, departure_date, adults, max_results):
    url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    headers = {
        'Authorization': f'Bearer {access_token}',
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




# Get tomorrow's date
tomorrow = datetime.now().date() + timedelta(days=70)

# Iterate over the next 180 days
for day in range((tomorrow + timedelta(days=10) - tomorrow).days):
    current_date = tomorrow + timedelta(days=day)
    print(current_date)
    

    fo = search_flight_offers(access_token, 'WAW', 'NYC', current_date, 1, 10)
    #pprint (fo)


    #iterate every day from tomorrow to +180 days

    try:
        if fo["meta"]["count"] > 0:
            print("Flight offers found:")
            for flight_offer in fo['data']:
                # print(flight_offer['itineraries'][0]['segments'][0]['departure']['iataCode'],'-->'
                #     ,flight_offer['itineraries'][0]['segments'][0]['arrival']['iataCode'])
                price = float(flight_offer['price']["grandTotal"])
                currency = flight_offer['price']["currency"]
                if price < 800:
                    print("Price is low:", price, currency, current_date)

        else:
            print("No flight offers found.")
    except:
        print("skipping ",current_date )
    time.sleep(0.5)

    # with open("data.json", "w") as file:
    #     json.dump(fo, file) 

