import requests

from random import randrange
'''

curl --location --request GET 'https://finance.yahoo.com/quote/now/analysis ' \
--header 'Cookie: B=a8achhdgjfutf&b=3&s=78'
'''

class SimpleRestClient():
    def __init__(self, requestBody = "", cred={}):
        self.body=requestBody
        self.credentials = cred
        self.response = None

    def getClient(self, url):
        # cookie =  "B=a8achhdgjfutf&b=3&s=78"
        header=   {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
            "cache-control": "max-age=0",
            "dnt": "1",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        }

        print("request : "+url)
        response= requests.get(url, verify=False, headers=header, timeout=30)
        return response

    def getResponse(self, url):
        # cookie =  "B=a8achhdgjfutf&b=3&s=78"
        # header=   {
        #     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        #     "accept-encoding": "gzip, deflate, br",
        #     "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
        #     "cache-control": "max-age=0",
        #     "dnt": "1",
        #     "sec-fetch-dest": "document",
        #     "sec-fetch-mode": "navigate",
        #     "sec-fetch-site": "none",
        #     "sec-fetch-user": "?1",
        #     "upgrade-insecure-requests": "1",
        #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
        # }

        print("request : "+ url)
        response= requests.get(url, verify=False, timeout=30)
        # print(response.text)
        return response.text

