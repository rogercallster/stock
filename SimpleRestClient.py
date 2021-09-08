import requests


class SimpleRestClient:
    def __init__(self, requestBody = "", cred={}):
        self.body=requestBody
        self.credentials = cred
        self.response = None

    def getClient(self, url):
        headers = {"Cookie":"B=a8achhdgjfutf&b=3&s=78"}
        return requests.get(url,headers)

