import requests
from datetime import date, timedelta
import logging
from dotenv import load_dotenv
from twilio_sms import send_message
import os


logging.basicConfig(level=logging.DEBUG)
load_dotenv()


yesterday = (date.today() - timedelta(days=1)).isoformat()
before_yesterday = (date.today() - timedelta(days=2)).isoformat()

STOCK = "TSLA"
NEWS_API_QUERY = "tesla"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_stock_data(api_key, stock):
    params = {"function":"TIME_SERIES_DAILY",
          "symbol":stock,
          "apikey":api_key,}

    r = requests.get(url="https://www.alphavantage.co/query",params=params)
    r.raise_for_status()
    data = r.json()
    #in case of reach API limits
    # data = {
    # "Meta Data": {
    #     "1. Information": "Daily Prices (open, high, low, close) and Volumes",
    #     "2. Symbol": "IBM",
    #     "3. Last Refreshed": "2024-06-26",
    #     "4. Output Size": "Compact",
    #     "5. Time Zone": "US/Eastern"
    # },
    # "Time Series (Daily)": {
    #     "2024-06-26": {
    #         "1. open": "171.2800",
    #         "2. high": "172.6800",
    #         "3. low": "170.4100",
    #         "4. close": "171.8700",
    #         "5. volume": "2779016"
    #     },
    #     "2024-06-25": {
    #         "1. open": "175.1400",
    #         "2. high": "175.7526",
    #         "3. low": "171.4200",
    #         "4. close": "172.6000",
    #         "5. volume": "4119267"
    #     },
    #     "2024-06-24": {
    #         "1. open": "175.0000",
    #         "2. high": "178.4599",
    #         "3. low": "174.1500",
    #         "4. close": "175.0100",
    #         "5. volume": "4864735"
    #     }}}
    return data


def get_news(api_key, query, extra_params= {}):
    params = {"q":query,
          "apiKey":api_key,}

    r = requests.get(url="https://newsapi.org/v2/everything",params={**params, **extra_params})
    r.raise_for_status()
    data = r.json()
    return data

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

data = get_stock_data = get_stock_data(STOCK_API_KEY,STOCK)
logging.debug(data)

yesterday_price = float(data["Time Series (Daily)"][yesterday]["4. close"])
before_yesterday_price = float(data["Time Series (Daily)"][before_yesterday]["4. close"])
logging.debug( 'yesterday_price='+ str(yesterday_price))
logging.debug( 'before_yesterday_price='+ str(before_yesterday_price))
price_change = (yesterday_price - before_yesterday_price) / before_yesterday_price * 100 

if abs(price_change) > 0.005:
    logging.warning("Get News")

    news_data = get_news(api_key=NEWS_API_KEY, query=COMPANY_NAME
                        , extra_params={"sortBy":"publishedAt", "language":"en"} )

    for a in news_data["articles"][:3]:
        logging.info(f'{a["title"]}\n{a["description"]}')
        msg = (
            f'{STOCK}: {"🔺" if price_change > 0 else "🔻"} {price_change:.2f}%\n'
            f'Headline: {a.get("title", "N/A")}.\n'
            f'Brief: {a.get("description", "N/A")}'
        )
        logging.debug(msg=msg)
        send_message(account_sid=os.getenv("TWILIO_ACCOUNT_SID"), auth_token=os.getenv("TWILIO_AUTH_TOKEN")
                 , from_=os.getenv("TWILIO_FROM"), to=os.getenv("TWILIO_TO"), message_body=msg)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

