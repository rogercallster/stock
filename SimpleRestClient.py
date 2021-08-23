import requests


class SimpleRestClient:
    def __init__(self, requestBody = "", cred={}):
        self.body=requestBody
        self.credentials = cred
        self.response = None

    def getClient(self, url):
        self.response = requests.get(url)
        print(self.response)
        return self.response

