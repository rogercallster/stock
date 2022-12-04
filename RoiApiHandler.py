
# import xmltojson
import xmltodict, json
import json
# pip install xmltojson
from SimpleRestClient import SimpleRestClient


class ROIPaths:
    def __init__(self):
        self.baseUrl = "https://roic.ai/"
        self.paths=["company/", "financials/", "transcripts/","classic/", "monitoring/"]

    '''
    Syntax: xmltojson.parse(xml_input, xml_attribs=True, item_depth=0, item_callback)

Parameters:

        xml_input can be either a file or a string.
        xml_attribs will include attributes if set to True. Otherwise, ignore them if set to False.
        item_depth is the depth of children for which item_callback function is called when found.
        item_callback is a callback function
    '''

    def getJsonFromUrl(self, ticker):
        ticker=ticker.upper()
        url=self.baseUrl+self.paths[0]+ticker
        restClient = SimpleRestClient()
        data  = restClient.getResponse(url)

        xpars = xmltodict.parse(data.text)
        obj = json.dumps(xpars)
        print(obj)
        return obj
roi = ROIPaths()
roi.getJsonFromUrl("GOOG")
