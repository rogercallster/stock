'''
This copy right property of please do not use without approval.

Facebook Intrinsic Value Calculation (FB Stock)

'''
import requests
import logging
from datetime import date
from enum import Enum

from Company import Company
from SimpleRestClient import SimpleRestClient


class Source(Enum):
    NASDAQ = "https://api.nasdaq.com/api/screener/stocks"


class CompanyMapHandler():
    def __init__(self):
        # get list of campany from DB and
        self.company = {}

    def getTickersFromStockExchange(self, file):
        if not file:
            file = "extra/nasdaq_screener_1629672200240.csv"
        with open(file, "r") as reader:
            lines = reader.readlines()
            counter = 0
            for line in lines:
                counter += 1
                if counter == 1:
                    continue
                symbol, name, country, ipoYear, sector, industry = line.strip().split(",")
                self.company[symbol.lower()] = Company(name=name, ticker=symbol, sector=sector, ipoYear=ipoYear,
                                                       industry=industry, date=date.today().strftime("%d/%m/%Y"))
        reader.close()
        print(self.company["now"])
        return self.company
