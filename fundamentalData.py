#!/usr/bin/env python3
import sys
import requests

import pandas as pd

#request consts
EARNINGS = "EARNINGS"
ANNUAL_EARNINGS = "ANNUAL_EARNINGS"
MONTHLY_EARNINGS = "MONTHLY_EARNINGS"
BALANCE_SHEET = "BALANCE_SHEET"
CASHFLOW = "CASH_FLOW"
OVERVIEW = "OVERVIEW"
INCOME_STATEMENT = "INCOME_STATEMENT"

symbol = ''
key = ''

switcher = None

class FundamentalData:

    def ExecuteCommand(self, command):
        print(command)
        return switcher[command]()

    def RequestData(self, _requestName):
        url = 'https://www.alphavantage.co/query?function={0}&symbol={1}&apikey={2}'.format(_requestName, self.symbol, self.key)
        r = requests.get(url)
        return r.json()

    #Data request functions
    def GetBalanceSheet(self):
        data = self.RequestData(BALANCE_SHEET)
        return data["annualReports"]
    def GetCashFlow(self):
        return self.RequestData(CASHFLOW)
    def GetCompanyOverview(self):
        return self.RequestData(OVERVIEW)
    def GetIncomeStatement(self):
        data = self.RequestData(INCOME_STATEMENT)
        return data["annualReports"]


    def GetAnnualEarnings(self):
        return self.GetEarnings(True)
    def GetMonthlyEarnings(self):
        return self.GetEarnings(False)

    #earnings helper
    def GetEarnings(self, IsAnnual = True):
        data = self.RequestData(EARNINGS)
        term = ''
        if IsAnnual == True:
            term = 'annualEarnings'
        else:
            term = 'quarterlyEarnings'

        annualEarnings = data[term]
        return annualEarnings

    def __init__(self, _symbol, _key):
        global switcher

        self.symbol = _symbol
        self.key = _key

        switcher = {
            ANNUAL_EARNINGS: self.GetAnnualEarnings,
            MONTHLY_EARNINGS: self.GetMonthlyEarnings,
            BALANCE_SHEET: self.GetBalanceSheet,
            OVERVIEW: self.GetCompanyOverview,
            INCOME_STATEMENT: self.GetIncomeStatement
        }
