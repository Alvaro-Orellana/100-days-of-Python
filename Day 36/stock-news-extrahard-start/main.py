import os
import requests
from dataclasses import dataclass
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
DESTINATION_NUMBER = '+56928121317'

@dataclass
class NewsArticle:
    title: str
    description: str

def get_stock_percent_change(stock_sticker: str) -> float:
    ## STEP 1: Use https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    alpha_avantage_api_key = os.environ.get('ALPHA_AVANTAGE_API_KEY')
    params = {"apikey":alpha_avantage_api_key, "function":"GLOBAL_QUOTE", "symbol":stock_sticker,}
    response = requests.get("https://www.alphavantage.co/query", params=params)
    response.raise_for_status()

    #TODO: check if this api returns negative percentages or only positive ones
    "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey=BE0TAZVO3KT9P0TK"

    percent_change = response.json()["Global Quote"]["10. change percent"]
    percent_change = percent_change.strip('%')
    return float(percent_change)

def get_company_news_articles(company_name: str) -> list[NewsArticle]:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api_key = os.environ.get('NEWS_API_KEY')
    params = {'apiKey': news_api_key, 'q': company_name, 'sortBy': 'popularity', 'pageSize': 3,}
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    response.raise_for_status()

    articles = response.json()["articles"]
    return [NewsArticle(article["title"], article["description"]) for article in articles]

if __name__ == '__main__':
    company_stock_price_change = get_stock_percent_change(STOCK)
    if company_stock_price_change > 5:
        # Send a seperate message with the percentage change and each article's title and description to your phone number.
        account_sid, auth_token = os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get("TWILIO_AUTH_TOKEN")
        twilio_client = Client(account_sid, auth_token)
        symbol = "🔺" if company_stock_price_change > 0 else "🔻" if company_stock_price_change < 0 else ""

        for article in get_company_news_articles(COMPANY_NAME):
            message = f"{STOCK}: {symbol}%\nHeadline: {article.title}\nBrief: {article.description}"
            twilio_client.messages.create(from_='+19522436053', body=message, to=DESTINATION_NUMBER)
