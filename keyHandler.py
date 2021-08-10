#!/usr/bin/env python3
import sys

key = ''

class KeyHandler:
    def __init__(self):
        keyFile = open("Key.txt", "r")
        self.key = keyFile.read()
        keyFile.close()

    def GetKey(self):
        return self.key
