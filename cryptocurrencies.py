#!/usr/bin/env python3
import sys

key = ''
symbol = ''

class Cryptocurrencies:
    def __init__(self, _key):
        print("Cryptocurrencies created")
        self.key = _key

    def PromptForCryptoSymbol(self):
        self.symbol = input("Name the Cryptocurrency: ").upper()
