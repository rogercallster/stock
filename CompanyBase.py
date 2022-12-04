class CompanyBase:
    '''

            https://roic.ai/company/GOOG


    '''
    def __init__(self, ticker):
        self.name=None
        self.ticker=ticker
        self.currentMarketCap=-1
        self.currentStockPrice=-1
        self.marginOfSafetyPrice = -1
        self.growthRate = -1
        self.currentFreeCashFlow = -1
        self.multipleOfFreeCashFlow = [i for i in range(1, 30)]
        self.discountRate = [i for i in  range(5,32)]
        self.currentDebt = -1
        self.currentIntrinsicValue = -1


