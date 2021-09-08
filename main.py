# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

'''
1) Calculate: PE RATIO
2) Equity
2) Calculate DEBT TO Equity ratio
3) FreeCash flow to Equity ration


'''
from CompanyMapHandler import CompanyMapHandler


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    t=CompanyMapHandler ()
    # //get list of companies with basic items filled.This will be map of Companies class
    # KEY : Name of company
    #value : ticker
    # this function takes in file name to generate map by default its file inside extra/nasdaq_screener_xxxxx.csv
    companieyMap = t.getTickersFromStockExchange(None)
    companieyMap.get("vmw").process()
    print((companieyMap.get("vmw")))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
