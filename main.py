#!/usr/bin/env python3
import sys

from fundamentalData import FundamentalData
from stockTimeSeries import StockTimeSeries
from cryptocurrencies import Cryptocurrencies
from keyHandler import KeyHandler
from uiHelper import UiHelper

from StockGui import StockguiApp

from pandas_datareader import data
import pandas as pd

import matplotlib.pyplot as plt
import requests

import tkinter as tk
import tkinter.ttk as ttk

key = ''
symbol = ''

app = None
uiHelper = None

def main():
    #global variables
    global app
    global uiHelper

    #initiate the key
    SetKey()

    #setup the User Interface
    root = tk.Tk()
    app = StockguiApp(root)
    uiHelper = UiHelper(app)

    #Setup User Interface Buttons
    ConfigureButtons()

    #Run User Interface
    app.run()

def ConfigureButtons():
    app.getFdData.configure(command=fundDataButtonHandler)

def fundDataButtonHandler():
    SetSymbol()
    fundData = FundamentalData(symbol, key)
    command = app.comboboxFD.get()
    data = fundData.ExecuteCommand(command)
    ClearTextBox(app.fdDataTree)
    uiHelper.GenerateTree(app.fdDataTree, data)

def ClearTextBox(_textBox):
    #_textBox.delete('1.0', "end")
    _textBox.delete(*_textBox.get_children())

def SetSymbol():
    global symbol
    symbol = app.stockSymbolEntry.get().upper()

def SetKey():
    global key
    key = KeyHandler().GetKey()

def ChangeStockSymbol(newSymbol):
    global symbol
    symbol = newSymbol.upper()

if __name__ == '__main__':
    main()
