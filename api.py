import requests
import json

"""
Calls to CoinDesk API. I need some information to pass to
the publisher and this sounds like a fun idea.

Powered by CoinDesk
https://www.coindesk.com/price/bitcoin
"""


class Api:
    def __init__(self) -> None:
        self.lastPrice = 0

    def callApi(self) -> int:
        """Returns direction of the price. -1 if down, 1 if up, 0 if the sideways"""
        json = self.getApiData()
        if json == -1:
            return
        return self.getDirectionOfPrice(self.getBtcPrice(json))

    def getApiData(self):
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            return response.json()
        else:
            print("API call had error " + str(response.status_code))
            return -1

    def getBtcPrice(self, json):
        usdPrice = json["bpi"]["USD"]["rate"]
        return float(usdPrice.replace(',',""))

    def getDirectionOfPrice(self, price):
        if price > self.lastPrice:
            self.lastPrice = price
            self.lastDirection = 1
            return 1
        if price < self.lastPrice:
            self.lastPrice = price
            return -1
        return 0




