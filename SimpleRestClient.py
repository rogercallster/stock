import requests


class SimpleRestClient:
    def __init__(self, url, requestBody = "", cred={}):
        self.url=url
        self.body=requestBody
        self.credentials = cred
        self.response = None

    def getClient(self):
        self.response = requests.get(self.url)
        print(self.response)
        return self.response

