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

from HTML_parser import HtmlParser
import jsonpickle


def readJsonFile(fileName="./extra/CompleteNasdaqList.json"):
    f = open(fileName)
    data = json.load(f)
    # for i in data['rows'][0]:
    #     print(i, data['rows'][0][i])
    return data['rows']


'''
symbol A
name Agilent Technologies Inc. Common Stock
lastsale $149.65
netchange -1.44
pctchange -0.953%
volume 699759
marketCap 44307180786.00
country United States
ipoyear 1999
industry Electrical Products
sector Industrials
'''

def listParcer(list):
    if list[0][-1]=='%':
        for i in list:
            list[i]=list[i][:-1]
    return list
def generateROICList(companies):
    companyList = []
    parser= HtmlParser()
    listOfCompanyNotFound = []
    # for company in companies:
    i=1
    for company in companies:
        print("index:" + str(i))
        i+=1
        result = parser.construct(company['symbol'], company)

        if result:
            companyList.append( result)
        else: listOfCompanyNotFound.append(company)
        # print(jsonpickle.encode((companyList[-1])))
    return companyList, listOfCompanyNotFound
    # companies.sort(key=lambda x:x['roic'])
def getOfLast5YearAve(arr):
    val = 0
    arr=arr[::-1]
    size=0
    for i in range(0, min(5,len(arr))):
        size+=1
        sign = 1
        if '-'  in arr[i] or "_" in arr[i]: break
        arr[i]=arr[i].strip()[:-1]
        if arr[i][0]=='(':
            sign=-1
            arr[i]=arr[i][1:-1]
        val+=float(arr[i].replace(",", ""))*sign

    return val/(min(size,len(arr)))

# print("hELLO .... \n\n HI")
companiesNameListFromJsonFile = readJsonFile("./extra/CompleteNasdaqList.json")
companies = []
listOfnotFoundCompany=[]
size=50
with open  ("/Users/asaran/dev/py/stock/tmp_"+str(datetime.now()) + ".json", "a") as tmp:

    for index in range(0, len(companiesNameListFromJsonFile), size):
        print("\n\nstart index :"+str(index))
        listOfCompanies, notFoundCompanies=generateROICList(companiesNameListFromJsonFile[index: index+size])
        companies.extend( listOfCompanies)
        listOfnotFoundCompany.extend(notFoundCompanies)
        print("Not found " + str(listOfnotFoundCompany))
        tmp.write(jsonpickle.encode(listOfCompanies) + "\n")
tmp.close()
# for comp in companies:
#     (comp.displayName, getOfLast5YearAve(comp.roicPercentage))
# print()
with open  ("/Users/asaran/dev/py/stock/NonSortedJson_"+str(datetime.now()) + ".json", "w") as result:
    result.write(jsonpickle.encode(companies))
result.close()
with open  ("/Users/asaran/dev/py/stock/CompaniesNotFound_"+str(datetime.now()) + ".json", "w") as result:
    result.write(jsonpickle.encode(notFoundCompanies))
result.close()


companies.sort(key=lambda x:-1*(getOfLast5YearAve(x.roicPercentage) if hasattr(x, 'roicPercentage')  else  0))

with open  ("/Users/asaran/dev/py/stock/SortedJson_"+str(datetime.now()) + ".json", "w") as result:
    result.write(jsonpickle.encode(companies))
result.close()

with open("/Users/asaran/dev/py/stock/sortedName" + str(datetime.now()) + ".json", "w") as result:
    result.write("Name, Symbol, debt \n")
    for company in companies:
        result.write(company.displayName+ ",  " + company.ticker + ", " +  company.totalDebt  + "\n")
result.close()
# for company in companies:
#     print(company.displayName, company.debt, company.roicPercentage)
#     print(jsonpickle.encode(company))






# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#     t=CompanyMapHandler ()
#     # //get list of companies with basic items filled.This will be map of Companies class
#     # KEY : Name of company
#     #value : ticker
#     # this function takes in file name to generate map by default its file inside extra/nasdaq_screener_xxxxx.csv
#     portfolio = ["now"]
#
#     companieyMap = t.getTickersFromStockExchange(None)
#     d={}
#     for company in portfolio:
#         d[company] = companieyMap[company.lower()]
#     companieyMap.get("vmw").process()
#     print((companieyMap.get("vmw")))
#     procesEachCompany(d)
#
# def procesEachCompany(companyMap):
#     format = "%d-%m-%y__%H-%M-%S"
#
#     date_time_str=datetime.now().strftime(format)
#     print(date_time_str)
#     with open(date_time_str, "w") as file:
#         for company in companyMap.keys():
#             print("Company -> ", company , "=============\t\t\t\t\t========\n\n")
#             s=(companyMap.get(company.lower()).process())
#             print(s)
#             # print("s json == ", json.dumps(s.to_json(s)))
#             # print("str  ", str(s) )
#             break
#             # file.write((s) +"\n")
#     file.close()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
