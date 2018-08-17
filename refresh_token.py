#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 14:35:16 2018

@author: bking
"""

import sys
import json
import requests

def get_access(refresh_token):
    url = "https://login.questrade.com/oauth2/token"
    querystring = {"grant_type":"refresh_token","refresh_token":refresh_token}
    headers = {
            'Cache-Control': "no-cache"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    json_data = json.loads(response.text)

    access_token = json_data['access_token']
    api_server = json_data['api_server']
    return access_token, api_server

### Example refresh token response ###
#example = {
#    "access_token": "aqFpAEoxhgCfQLJvWTNM5h8bM2kUEVe50",
#    "api_server": "https://api02.iq.questrade.com/",
#    "expires_in": 1800,
#    "refresh_token": "DN6pAOSz5hvUxaIOYDjfd2E5kqGWKfDi0",
#    "token_type": "Bearer"
#}

refresh = str(sys.argv[1])


if refresh == "refresh":
    refresh_token = input("Enter your refresh token:")
    access_token, api_server = get_access(refresh_token)
    print ("Use access token and server information from access.txt and server.txt")
    
    with open('access.txt', 'w') as f:
         print(access_token[::-1], file=f)
    
    with open('server.txt', 'w') as f:
         print(api_server[::-1], file=f)
    
else:
    
    print("To get access token and server information, use $ python3 refresh_token.py refresh")