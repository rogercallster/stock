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
from datetime import  datetime
import json
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    t=CompanyMapHandler ()
    # //get list of companies with basic items filled.This will be map of Companies class
    # KEY : Name of company
    #value : ticker
    # this function takes in file name to generate map by default its file inside extra/nasdaq_screener_xxxxx.csv
    portfolio = ["now"]

    companieyMap = t.getTickersFromStockExchange(None)
    d={}
    for company in portfolio:
        d[company] = companieyMap[company.lower()]
    companieyMap.get("vmw").process()
    print((companieyMap.get("vmw")))
    procesEachCompany(d)

def procesEachCompany(companyMap):
    format = "%d-%m-%y__%H-%M-%S"

    date_time_str=datetime.now().strftime(format)
    print(date_time_str)
    with open(date_time_str, "w") as file:
        for company in companyMap.keys():
            print("Company -> ", company , "=============\t\t\t\t\t========\n\n")
            s=(companyMap.get(company.lower()).process())
            print(s.)
            # print("s json == ", json.dumps(s.to_json(s)))
            # print("str  ", str(s) )
            break
            # file.write((s) +"\n")
    file.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
