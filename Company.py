'''
This copy right property of please do not use without approval.
'''


class Company():

    def __init__(self, name, ticker, price, date, peRatio, debt, equity, freeCashFlow, growthRate):
        self.displayName = name
        self.ticker = ticker
        self.stockPrice = price
        self.equity = equity
        self.date = date
        self.peRatio = peRatio
        self.marginOfSaftyPrice
        self.debt = debt
        self.freeCashFlow = freeCashFlow
        self.growthRate = growthRate

    # todo calculate it
    def getMarginOfSafty(self):

        self.marginOfSaftyPrice=0# todo
        return self.marginOfSaftyPrice
