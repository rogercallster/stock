'''
This copy right property of please do not use without approval.

Symbol	Name	Last Sale	Net Change	% Change	Market Cap	Country	IPO Year	Volume	Sector	Industry
'''

from enum import Enum


class BuyingOption(Enum):
    BUY = "buy"
    DONT_BUY = "dont buy"
    RISKY = "risky"
    CANT_UNDERSTAND = "cannot understand"
    DID_NOT_EVALUATE = "did not evaluate yet"


class Company():
    def __init__(self, name, ticker, price=-1, date=None, peRatio=None, debt=None, equity=None, freeCashFlow=None,
                 growthRate=None, marketCap=None, ipoYear="1900",
                 volume=None, sector="", industry=""):
        self.displayName = name
        self.ticker = ticker
        self.stockPrice = price
        self.equity = equity
        self.date = date
        self.peRatio = peRatio
        self.marginOfSaftyPrice = 0.0
        self.debt = debt
        self.freeCashFlow = freeCashFlow
        self.growthRate = growthRate
        self.marketCap = marketCap
        self.ipoYear = ipoYear
        self.volume = volume
        self.sector = sector
        self.industry = industry
        self.buyingOption = BuyingOption.DID_NOT_EVALUATE

    # todo calculate it
    def getMarginOfSafty(self):
        self.marginOfSaftyPrice = 0  # todo
        return self.marginOfSaftyPrice

    def fillBuyingOption(self):
        pass

    def tenYearDiscountPrice(self):
        pass

    def fiveYearDiscountPrice(self):
        pass

    def fillPERation(self):
        pass

    def fillFreeCashFlow(self):
        pass

    def fillGrowthRate(self):
        pass

    def filEquity(self):
        pass
