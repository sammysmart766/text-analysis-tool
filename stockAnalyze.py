import yfinance as yf
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
    print(prices.to_string())


def getEarningsDate(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    earningsDates = company.get_earnings_dates(limit=12)
    futureDates = earningsDates[earningsDates.index.date >= date.today()]
    for earningsDate in futureDates.index:
        print('EARNINGS DATE: '+ str(earningsDate.date()))

def getCompanyNews(tickerSymbol):
    articles = yf.Search(tickerSymbol, news_count=10).news

    for article in articles:
        print(article["title"])
        print(article["link"])
        print()


def getCompanyStockInfo(tickerSymbol):
    company = yf.Ticker(tickerSymbol)
    basicInfo = extractBasicInfo(company.info)

    print(basicInfo)
    priceHistory = getDailyPriceHistory(tickerSymbol)
    EarningsDate = getEarningsDate(tickerSymbol)
    CompanyNews = getCompanyNews(tickerSymbol)


getCompanyStockInfo("MSFT")
