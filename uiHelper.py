#!/usr/bin/env python3
import sys
import requests

import pandas as pd

app = None

class UiHelper:

    def __init__(self, _app):
        self.app = _app

    #Generate a tree with headings and values given an
    #empty tree and dictionary of data
    def GenerateTree(self, _tree, _dataDump):
        #demo dictionary   [
        #                   {value1:"incomeYear", value2:"dsad", value3: "dsad"},
        #                   {value4:"dsad", value5:"dsad", value6:"dsasa"}
        #                  ]

        #set Column Names
        _tree['columns'] = tuple(_dataDump[0].keys())

        #initial column setup
        _tree.heading("#0", text="")
        _tree.column("#0", width=0, minwidth=0)

        #add/edit column headings
        for columnName in _tree['columns']:
            #columnName
            columnNameLen = len(columnName)
            columnWidth = 0
            if(columnNameLen <= 6):
                columnWidth = 50
            elif(columnNameLen > 6 and columnNameLen <= 9):
                columnWidth = 75
            elif(columnNameLen > 9 and columnNameLen <= 13):
                columnWidth = 130
            else:
                columnWidth = 180

            _tree.column(column=columnName, anchor='w', width=columnWidth)
            _tree.heading(columnName, text=columnName)


        #insert values
        counter = 0
        for list in _dataDump:
            listOfValues = tuple(list.values())
            #if you want commas in the numbers -->
            #write a function that takes in the current
            #list of values. Loop through the values and
            #determine if the value isDigit. If is Digit
            #then format the value based on f'{value:,}'
            _tree.insert(parent = '', index='end', iid = counter, text="", value=listOfValues[0:])
            counter += 1
