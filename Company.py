'''
This copy right property of please do not use without approval.
'''

'''
Equity :  Equity indicates an ownership position in an asset. In most cases, equity indicates a total ownership stake in
 a company. So if, for example, you have a 15% equity in a company, you own 15% of that company and are entitled to 15%
 of the company’s profits. An equity investment is typically purchased with the expectation that the value of the invest
 -ment will increase over time. For instance,when you have equity in a business, you expect the value of the business to
 increase in value so that you can benefit from your stake in the business. By having equity, you are essentially stakin
 -g your money on the company’s future success.

Stocks (Common, Preferred ):While equity describes ownership, a stock describes a single unit of that ownership share.
 The more stock you buy, the more your equity. Put simply, a stock is the means with which you can engage in company equ
 -ity transactions. Stocks are generally a tradable form of equity that was created to facilitate the exchange of owners
 -hip value in an open market. They might refer to energy stocks, value stocks, large- or small-cap stocks, food-sector
 stocks, blue-chip stocks, etc. The stocks are traded on large public exchanges and sometimes they are traded in private
 offerings. When you buy stocks, you are buying equity in a company from someone selling part of or all of their owners
 -hip stake in the company. When you sell stocks, you are selling your equity to someone who wants to buy art of or all
 of your ownership stake. There are two main types of stock that companies issue:

'''

from enum import Enum


class BuyingOption(Enum):
    BUY = "buy"
    DONT_BUY = "dont buy"
    RISKY = "risky"
    CANT_UNDERSTAND = "cannot understand"
    DID_NOT_EVALUATE = "This stock is not yet evaluated"


class Company():
    def __init__(self, name, ticker, price=-1, date=None, peRatio=0, debt=0.0, freeCashFlow={},
                 growthRate={}, marketCap=0.0, ipoYear="1900",
                 volume=None, sector="", industry=""):
        self._displayName = name
        self._ticker = ticker
        self._stockPrice = price
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
    def stockPrice(self, price):
        self._stockPrice = price

    @property
    def peRation(self):
        return self._peRatio

    @peRation.setter
    def peRation(self, ratio):
        self._peRatio = ratio

    @property
    def debt(self):
        return self._debt

    @debt.setter
    def debt(self, debt):
        self._debt = debt

    @property
    def freeCashFlow(self):
        return self._freeCashFlow

    @freeCashFlow.setter
    def freeCashFlow(self, freeCashFlow):
        self._freeCashFlow = freeCashFlow

    @property
    def growthRate(self):
        return self._growthRate

    @growthRate.setter
    def growthRate(self, growthRate):
        self._growthRate = growthRate

    @property
    def marketCap(self):
        return self._marketCap

    @marketCap.setter
    def marketCap(self, capVal):
        self._marketCap = capVal

    @property
    def date(self):
        return self._date

    @property
    def buyingOption(self):
        return self._buyingOption

    @buyingOption.setter
    def buyingOption(self, buyingOption):
        self._buyingOption = buyingOption

    '''
self._displayName = name
        self._volume = volume
        self._buyingOption = BuyingOption.DID_NOT_EVALUATE
    '''

    def __str__(self):
        return "{ " + "'Name':'" + self.displayName + "', 'Symbol':'" + self.ticker + "', 'sector':" + self.sector \
               + "', 'ipoYear':'" + self.ipoYear + "', 'industry':'" + self.industry + "', 'price':" + str(
            self.stockPrice) + ", 'peRation':" + str(
            self.peRation) + ", 'marginOfSaftyPrice': " + str(self.marginOfSaftyPrice) + ", 'debt':" + str(
            self.debt) + ", 'freeCashFlow':" + str(self.freeCashFlow) + ", 'growthRate':" + str(
            self._growthRate) + ", 'marketCap':" + str(
            self.marketCap) + ", 'date':" + self.date + ", 'buyingOption':'" + str(self.buyingOption.value) + "' }"
