import yfinance as yf
import requests
from datetime import date

def extractBasicInfo(data):
    keysToExtract = [
        "longName", "website", "sector", "fullTimeEmployees", "marketCap", "totalRevenue", "trailingEps"]
    basicInfo = {}

    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
        else:
            basicInfo[key] = ""

    return basicInfo


def getDailyPriceHistory(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    hist = company.history(period="12mo", interval="1d")
    prices = hist[["Open"]]
    return prices


def getEarningsDate(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    earningsDates = company.get_earnings_dates(limit=12)
    futureDates = earningsDates[earningsDates.index.date >= date.today()]
    return futureDates

def getCompanyNews(tickerSymbol):
    articles = yf.Search(tickerSymbol, news_count=10).news
    return articles

    for article in articles:
        print(article["title"])
        print(article["link"])
        print()
        
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36' 
}
def extractCompanyNewsArticle(companynews):
    url = companynews[0]['link']
    page = requests.get(url, headers=headers)
    print(page.text)
    #print(url)

def getCompanyStockInfo(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    basicInfo = extractBasicInfo(company.info)

    
    priceHistory = getDailyPriceHistory(tickerSymbol)
    earningsDate = getEarningsDate(tickerSymbol)
    companynews = getCompanyNews(tickerSymbol)
    extractCompanyNewsArticle(companynews)

getCompanyStockInfo("MSFT")
