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

import yfinance as yf
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
        self._totalDebt = debt
        self._freeCashFlow = freeCashFlow
        self._growthRate = growthRate
        self._marketCap = marketCap
        self._ipoYear = ipoYear
        self._volume24Hr = volume
        self._sector = sector
        self._industry = industry
        self._buyingOption = BuyingOption.DID_NOT_EVALUATE

        self._revenue = 0.0
        self._info = {}
        #below are not used and park of info
        # self._epm = 0.0
        # self._operatingCashflow = 0.0
        # self._revenueGrowth = 0.0
        # self._operatingMargins = 0.0
        # self._ebitda = 0.0  # earnings before interest, taxes, depreciation, and amortization
        # self._grossProfits = 0.0
        # self._freeCashflow = 0.0
        # self._earningsGrowth = 0.0
        # # The _currentRatio is a measure of how likely a company is to be able to pay its debts in the short term.
        # # Short-term debts are generally money owed within a year. It is essentially a liquidity ratio, measuring a
        # # firm’s assets versus how much it owes.
        # self._currentRatio = 0.0
        # self._numberOfAnalystOpinions = 0.0
        # self._debtToEquity = 0.0
        # self._returnOnEquity = 0.0
        # self._totalCash = 0.0
        # self._totalRevenue = 0.0
        # self._totalCashPerShare = 0.0
        # # The quick ratio measures how well a company can meet its short-term liabilities.
        # # The quick ratio (QR) is calculated through the following formula:
        # # QuickRatio = (Cash and Cash Equivalent + Liquid Securities + Accounts Receivable) / Short-Term Liabilities
        # self._revenuePerShare = 0.0
        # self._exchange = ""
        # self._enterpriseToEbitda = 0.0
        # #
        # self._52WeekChange = 0.0
        # self._morningStarRiskRating="None"
        # self._bookValue =  0.0
        # self._sharesShort =0.0
        # self._trailingEps = 0.0
        # self._lastDividendValue =0.0
        # self._shortRatio = 0.0
        # self._threeYearAverageReturn = 0.0
        # self._earningsQuarterlyGrowth = 0.0
        # self._priceToSalesTrailing12Months =0.0
        # # “PEG” stands for price-earnings-to-growth. The price-earnings-to-growth ratio is calculated through the basic formula:
        # #
        # #     PEG = (price-to-earnings ratio) / (expected earnings growth rate)
        # self._pegRatio = 0.0
        # self._forwardPE = 0.0
        # self._averageDailyVolume10Day=0
        # self._regularMarketVolume = 0
        # self._averageVolume =0
        # self._volume = 0
        #


    ''' 
    generates:
        1) StockPrice
        2) peRatio
        3) debt
        4) freeCashFlow
        5) growthRate
        6)marketCap
        7) volume
        8) buyingOption
        
    '''



    def process(self):
        info=self.info
        # print(info)

        for key in ( info.keys()):
            print(key, info[key])
            # print(key, info(key))

        # self.stockPrice= info.get("currentPrice")
        # self.peRation = info.get("trailingPE") # or self.peRation(self.info("forwardPE"))
        # self.freeCashFlow = info.get("freeCashflow")
        # # self.growthRate = info.get()
        print(self)


    @property
    def info(self):
        value=yf.Ticker(self.ticker)
        self._info = value.get_info()
        return self._info
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
    def totalDebt(self):
        return self._totalDebt

    @totalDebt.setter
    def totalDebt(self, totalDebt):
        self._totalDebt = totalDebt

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
            self.totalDebt) + ", 'freeCashFlow':" + str(self.freeCashFlow) + ", 'growthRate':" + str(
            self._growthRate) + ", 'marketCap':" + str(
            self.marketCap) + ", 'date':" + self.date + ", 'buyingOption':'" + str(self.buyingOption.value) + "' }"
