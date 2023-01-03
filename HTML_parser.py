import json

from bs4 import BeautifulSoup
from lxml import etree
import jsonpickle
from Company import Company
from SimpleRestClient import SimpleRestClient

'''
https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/

'''

'''
https://www.twilio.com/blog/web-scraping-and-parsing-html-in-python-with-beautiful-soup
1)
vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

2) 
The find() and find_all() methods are among the most powerful weapons in your arsenal. soup.find() is great for cases where you know there is only one element you're looking for, such as the body tag. On this page, soup.find(id='banner_ad').text will get you the text from the HTML element for the banner advertisement.

soup.find_all() is the most common method you will be using in your web scraping adventures. Using this you can iterate through all of the hyperlinks on the page and print their URLs:

for link in soup.find_all('a'):
    print(link.get('href'))
    attrs = {
        'href': re.compile(r'\.mid$')
    }
    tracks = soup.find_all('a', attrs=attrs, string=re.compile(r'^((?!\().)*$'))
    
    
'''

'''
xpath of interest = dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[3]/div[1]/div[1]/h1")[0].text
'''


class HtmlParser():
    def __init__(self):
        self.response = None

    def getSoup(self, ticker):
        ticker = ticker.upper()
        simpleRestClient = SimpleRestClient()
        # company for summary
        restResponse = simpleRestClient.getResponse("https://roic.ai/" + "company/" + ticker)
        # print("RestResponse " , restResponse)
        return BeautifulSoup(restResponse, 'html.parser')

    def getDom(self, ticker):
        soup = self.getSoup(ticker)
        dom = etree.HTML(str(soup))
        return dom

    def domArrayParser(self, dom, xpath, index=1):
        # print("xpath ", xpath)
        result = []
        i = index
        # /html/body/div/div/main/div[3]/div/div[1]/div/div[3]/div[2]/div[5]
        path = xpath + "[" + str(i) + "]"
        while dom.xpath(path) != None:

            try:
                element = dom.xpath(path)[0].text
                # if not element.isnumeric(): continue
                path = xpath + "[" + str(i) + "]"
                i += 1
                # print(element)
                result.append(element)
            except:
                # print("reached index end ", str(i))
                return result

    def fillCompanyDetails(self, ticker, company):
        if "^" in ticker:
            print("Ticker before " + ticker + " ticker after trim = "+ ticker[:-2])
            ticker = ticker[:-2]
        if "/" in ticker:
            print("change " + ticker  + " " + ticker.replace("/","-"))
            ticker=ticker.replace("/","-")

        try:
            dom = self.getDom(ticker)
            name = dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[2]/div[2]/h1")[0].text
            # print("name ", name)
            stockPrice = float(dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[3]/div[1]/div[1]/h1")[0].text)
            # print("stockPrice ", stockPrice)
            marketCap = (dom.xpath("/html/body/div[1]/div/main/div[2]/div[1]/div[3]/div[3]/div[4]/span[1]")[0].text)
            # print("Market cap: ", marketCap)
            peRatio = float(dom.xpath("/html/body/div[1]/div/main/div[2]/div[1]/div[3]/div[3]/div[1]/span[1]")[0].text)
            # print("P/E ration ", peRatio)
            peRatioSnp500 = dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[3]/div[3]/div[3]/span[1]")[0].text
            # print("P/E to SNP 500  ", peRatioSnp500)
            nextEarningCall = dom.xpath("/html/body/div/div/main/div[3]/div/div[1]/div/div[1]/div[1]/div[1]/div[3]")[0].text
            # print("Next earning call ", nextEarningCall)

            shareVolume = float(
                dom.xpath("/html/body/div/div/main/div[3]/div/div[1]/div/div[1]/div[1]/div[11]/div[3]")[0].text) * 1000000
            # print("Volume ", shareVolume)

            # /html/body/div/div/main/div[3]/div/div[1]/div/div[3]/div[1]/span
            # /html/body/div/div/main/div[3]/div/div[1]/div/div[3]/div[2]/div[5]
            # /html/body/div/div/main/div[3]/div/div[1]/div/div[3]/div[2]/div[6]
            years = self.domArrayParser(dom, "/html/body/div/div/main/div[3]/div/div[1]/div/div[2]/div[2]/div", 5)
            revenuePerShare = self.domArrayParser(dom, "/html/body/div/div/main/div[3]/div/div[1]/div/div[3]/div[2]/div", 5)
            fcfPerShare = self.domArrayParser(dom, "/html/body/div/div/main/div[3]/div/div[1]/div/div[5]/div[2]/div", 5)
            capexPerShare = self.domArrayParser(dom, "/html/body/div/div/main/div[3]/div/div[1]/div/div[7]/div[2]/div", 5)
            bookValuePerShare = self.domArrayParser(dom,"/html/body/div/div/main/div[3]/div/div[1]/div/div[8]/div[2]/div", 5)
            netProfitMarginPerShare = self.domArrayParser(dom,"/html/body/div[1]/div/main/div[3]/div/div[1]/div/div[18]/div[2]/div", 5)
            # debt = self.domArrayParser(dom,"/html/body/div[1]/div/main/div[3]/div/div[1]/div/div[20]/div[2]/div", 5)
            returnOnCapitalPercentage = self.domArrayParser(dom,"/html/body/div/div/main/div[3]/div/div[1]/div/div[24]/div[2]/div", 5)
            # //*[@id="__next"]/div/main/div[3]/div/div[1]/div/div[22]/div[2]/div[3]
            roicPercentage = self.domArrayParser(dom,"/html/body/div/div/main/div[3]/div/div[1]/div/div[22]/div[2]/div", 5)[:-1]
            debt = "NA"
            if "-" not in dom.xpath("/html/body/div/div/main/div[3]/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/text()[2]")[0]:
                debt =float( dom.xpath("/html/body/div/div/main/div[3]/div/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/text()[2]")[0].strip().replace(",",""))/1000
            company = Company(dom=dom, ticker=ticker, name=name, price=stockPrice, marketCap=marketCap, peRatio=peRatio,
                              shareVolume=shareVolume,
                              peRatioSnp500=peRatioSnp500, years=years, revenuePerShare=revenuePerShare,
                              fcfPerShare=fcfPerShare, capexPerShare=capexPerShare, bookValuePerShare=bookValuePerShare,
                              netProfitMarginPerSharePercentage=netProfitMarginPerShare, debt=debt, returnOnCapitalPercentage=returnOnCapitalPercentage,
                              roicPercentage = roicPercentage,

                              )
        except Exception as e:
            print("Ticker::  " + ticker + " NAME: " + company["name"])
            print(e)
            return None
            # company = Company(name=company["name"], ticker=company["symbol"], debt=1000000, roicPercentage=["(10000)%","(10000)%","(10000)%","(10000)%","(10000)%"])


        return company



    def construct(self, ticker, company):
        # print(jsonpickle.encode(htmlParser.fillCompanyDetails(i)))
        htmlParser= HtmlParser()
        return htmlParser.fillCompanyDetails(ticker, company)

# htmlParser = HtmlParser()
# for i in ["GOOG"]:
    # print(json.dumps(htmlParser.fillCompanyDetails(i)))
    # print(json.loads(htmlParser.fillCompanyDetails(i)))
    # print((htmlParser.fillCompanyDetails(i)))
    # print(jsonpickle.encode(htmlParser.fillCompanyDetails(i)))
    # soup = htmlParser.getSoup(i)
    # dom = etree.HTML(str(soup))
    # print("name " , dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[2]/div[2]/h1")[0].text)
    # print("price ", dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[3]/div[1]/div[1]/h1")[0].text)
    # print("Market cap: ", dom.xpath("/html/body/div[1]/div/main/div[2]/div[1]/div[3]/div[3]/div[4]/span[1]")[0].text)
    # print("P/E ration ", dom.xpath("/html/body/div[1]/div/main/div[2]/div[1]/div[3]/div[3]/div[1]/span[1]")[0].text)
    # print("P/E to SNP 500  ", dom.xpath("/html/body/div/div/main/div[2]/div[1]/div[3]/div[3]/div[3]/span[1]")[0].text)
    # print("Next earning call ", dom.xpath("/html/body/div/div/main/div[3]/div/div[1]/div/div[1]/div[1]/div[1]/div[3]")[0].text)
    # print("Volume ", float(dom.xpath("/html/body/div/div/main/div[3]/div/div[1]/div/div[1]/div[1]/div[11]/div[3]")[0].text)*1000000)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
    # print(" ", dom.xpath("")[0].text)
ticker="AAIN"
p=HtmlParser()
# ob=            {
#                 "symbol": "AAIN",
#                 "name": "Arlington Asset Investment Corp 6.000% Senior Notes Due 2026",
#                 "lastsale": "$23.50",
#                 "netchange": "0.03",
#                 "pctchange": "0.128%",
#                 "volume": "511",
#                 "marketCap": "0.00",
#                 "country": "United States",
#                 "ipoyear": "",
#                 "industry": "Finance/Investors Services",
#                 "sector": "Finance",
#                 "url": "/market-activity/stocks/aain"
#             }
# ob={}
# ob={"symbol":"AAIN", "name":""}
#
# p.fillCompanyDetails(ticker,ob )
# ob={"symbol":"BKDT", "name":"Brookdale Senior Living Inc. 7.00% Tangible Equity Units"}
# p.fillCompanyDetails(ticker,ob )

# ob={"symbol":"GOOG", "name":"google"}
# p.fillCompanyDetails(ob["symbol"],ob )