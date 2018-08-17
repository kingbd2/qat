#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Toolkit for interacting with Questrade API

If you need to refresh an expired access token, run the file with "refresh" "<refresh_token>" as inputs. 

Created on Fri Aug 17 11:06:54 2018

@author: bking
"""

import sys
import json
import requests

with open('access.txt') as f:
    access_token = f.read().strip()
    access_token = access_token[::-1]
    
with open('server.txt') as f:
    api_server = f.read().strip()
    api_server = api_server[::-1]

def get_accounts(write, access_token, api_server):
    url = api_server + "v1/accounts"
    headers = {
        'Authorization': "Bearer " + access_token,
        'Cache-Control': "no-cache",
        }
    response = requests.request("GET", url, headers=headers)
    json_data = json.loads(response.text)
    
    if write =='w':
        with open('account_history.txt', 'a') as f:
            print(json_data, file=f)
    else:
        pass
    
    return json_data

def get_positions(account, access_token, api_server):
        url = api_server + "v1/accounts/" + account + "/positions"
        headers = {
            'Authorization': "Bearer " + access_token,
            'Cache-Control': "no-cache",
            }
        response = requests.request("GET", url, headers=headers)
        json_data = json.loads(response.text)
        
        with open('position_history.txt', 'a') as f:
             print(json_data, file=f)
        
        return json_data

def get_symbol(symbol, access_token, api_server):
    url = api_server + "v1/symbols/" + symbol
    headers = {
        'Authorization': "Bearer " + access_token,
        'Cache-Control': "no-cache",
        }
    response = requests.request("GET", url, headers=headers)
    json_data = json.loads(response.text)
    
    with open('symbol_history.txt', 'a') as f:
     print(json_data, file=f)

    return json_data

## Decision tree ##
decision = str(input("Do you want to collect account data?"))


if decision == 'y' or decision == 'Y' or decision=="yes":
    ### Fill account information to get positions of all accounts ###
    accounts = get_accounts('w', access_token, api_server)
    tfsa = accounts['accounts'][0]['number']
    rrsp = accounts['accounts'][1]['number']
    
    tfsa_positions = get_positions(tfsa, access_token, api_server)
    rrsp_positions = get_positions(rrsp, access_token, api_server)
 
    options = input("Do you want to get all of the symbols in your portfolio?")
    
    if options == 'y' or options == 'Y' or options == "yes":
        symbolIds = []
        for i, x in enumerate(tfsa_positions['positions']):
            symbolIds.append(tfsa_positions['positions'][i]['symbolId'])
        for i, x in enumerate(rrsp_positions['positions']):
            symbolIds.append(rrsp_positions['positions'][i]['symbolId'])
        
        symbol_collection = []
        for i, x in enumerate(symbolIds):
            symbol_collection.append(get_symbol(str(symbolIds[i]), access_token, api_server))
    
    else:
        symbol = input("Provide symbol ID:")
        get_symbol(symbol, access_token, api_server)  
    

else:
    accounts = get_accounts('w', access_token, api_server)
    tfsa = accounts['accounts'][0]['number']
    rrsp = accounts['accounts'][1]['number']
    
    tfsa_positions = get_positions(tfsa, access_token, api_server)
    rrsp_positions = get_positions(rrsp, access_token, api_server)
 
    options = input("Do you want to get all of the symbols in your portfolio?")
    
    if options == 'y' or options == 'Y' or options == "yes":
        symbolIds = []
        for i, x in enumerate(tfsa_positions['positions']):
            symbolIds.append(tfsa_positions['positions'][i]['symbolId'])
        for i, x in enumerate(rrsp_positions['positions']):
            symbolIds.append(rrsp_positions['positions'][i]['symbolId'])
        
        symbol_collection = []
        for i, x in enumerate(symbolIds):
            symbol_collection.append(get_symbol(str(symbolIds[i]), access_token, api_server))
    
    else:
        while True:
            symbol = input("Provide symbol ID:")
            if symbol == 'no':
                break
            else:
                get_symbol(symbol, access_token, api_server)  
    
#td = '38938'

#def hello():
#    print ("What?")

#if __name__ == '__main__':
#    hello()
