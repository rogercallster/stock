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
        self._displayName = name
        self._ticker = ticker
        self._stockPrice = price
        self._equity = equity
        self._date = date
        self._peRatio = peRatio
        self._marginOfSaftyPrice = 0.0
        self._debt = debt
        self._freeCashFlow = freeCashFlow
        self._growthRate = growthRate
        self._marketCap = marketCap
        self._ipoYear = ipoYear
        self._volume = volume
        self._sector = sector
        self._industry = industry
        self._buyingOption = BuyingOption.DID_NOT_EVALUATE

    # todo calculate it
    @property
    def marginOfSafty(self):
        return self._marginOfSaftyPrice

    # todo some logic required
    @marginOfSafty.setter
    def marginOfSaftyPrice(self, price):
        self._marginOfSaftyPrice = price

    @property
    def buyingOption(self):
        self._buyingOption

    @buyingOption.setter
    def buyingOption(self, option):
        # TODO some logic required
        self._buyingOption = option

    @property
    def displayName(self):
        return self._displayName

    @property
    def ticker(self):
        return self._ticker

    @property
    def industry(self):
        return self._industry

    @property
    def sector(self):
        return self._sector

    @property
    def ipoYear(self):
        return self._ipoYear

    @property
    def stockPrice(self):
        return self._stockPrice
    @stockPrice.setter
    def stockPrice(self , price):
        self._stockPrice = price

    def __str__(self):
        return "{" + "'Name':'" + self.displayName + "', 'Symbol':'" + self.ticker + "', 'sector':" + self.sector \
               + "', 'ipoYear':'" + self.ipoYear + "', 'industry':'" + self.industry +  "', 'price':'" + str(self.stockPrice)  + "'}"
