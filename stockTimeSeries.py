#!/usr/bin/env python3
import sys

import requests

import pandas as pd

symbol = ''
key = ''

TIME_SERIES_INTRADAY = "TIME_SERIES_INTRADAY"

class StockTimeSeries:
    def __init__(self, _symbol, _key):
        self.symbol = _symbol
        self.key = _key
        print('Time Series created')

    def RequestData(self, _function, _interval, _compact = 'compact'):
        url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&interval={2}&outputsize={3}&apikey={4}'.format(_function, self.symbol, _interval, _compact, self.key)
        r = requests.get(url)
        return r.json()

    def GetIntradayStockInfo(self, _timePeriod):
        return(self.convertListOfDictsToPandas(self.RequestData(TIME_SERIES_INTRADAY, _timePeriod, 'compact'), _timePeriod))

    def convertListOfDictsToPandas(self, listOfDicts, _timePeriod):
            newList = listOfDicts.get('Time Series ({0})'.format(_timePeriod))
            finalList = pd.DataFrame(newList)
            return finalList.transpose()
