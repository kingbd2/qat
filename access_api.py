#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Questrade API access application.

Created on Tue Apr 17 23:21:45 2018

@author: bking
"""
import requests

# STEP 1: Login to Questrade Developers using username and password. Register personal app. Generate refresh token. Copy refresh token. Go to https://login.questrade.com/oauth2/token?grant_type=refresh_token&refresh_token=<refresh_token>. Copy credentials.

server = "https://api07.iq.questrade.com/v1/"

class api:
    def __init__(self, refresh_token, server):
        self.refresh_token = refresh_token
        self.server = server
        
    #def register_app():
        
    def get_symbol(symbol):
        uri = server + "symbols/" + str(symbol)
        

credentials = {"access_token":"z_Z2aOccNb2sQVkFG5S-zFhWAF7KQ4B20","api_server":"https:\/\/api07.iq.questrade.com\/","expires_in":1800,"refresh_token":"mWcvwpS1X9d0igDEgDbN7mF_h1Kx6MXN0","token_type":"Bearer"}

## TD symbolID = 38938
uri = "https://api07.iq.questrade.com/v1/symbols/38938"
headers = {'Authorization': 'Bearer z_Z2aOccNb2sQVkFG5S-zFhWAF7KQ4B20'}

#GET /v1/accounts HTTP/1.1
host = "https://api07.iq.questrade.com"
#Authorization: Bearer C3lTUKuNQrAAmSD/TPjuV/HI7aNrAwDp


#Get symbol data

payload = {'accountNumber': 31455565, 
           'symbolId': 8049, 
           'quantity': 10, 
           'icebergQuantity': 1, 
           'limitPrice': 10, 
           'isAllOrNone': True, 
           'isAnonymous': False, 
           'timeInForce': "GoodTillCanceled", 
           'primaryRoute': "Auto", 
           'secondaryRoute': "Auto", 
           'orderType': "Limit"}

r = requests.get(uri, headers=headers)
response = r.json()

print (response)

## NEXT STEPS: CREATE CELERY TASKS TO CALL THE ABOVE SYMBOL REGULARLY TO PLOT TD STOCK PRICES

