import requests
from dotenv import load_dotenv
import os

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


search_iata_by_city_name(access_token, 'Warsaw')