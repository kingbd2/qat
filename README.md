#QAT - The Questrade API Toolkit
##Also, the easiest Q word in Scrabble.

To use this toolkit:
0. Create Questrade Personal App at https://www.questrade.com/api and generate refresh token (must have Questrade account).
1. Clone this repository and run pipenv install.
2. Run refresh_token.py - you will be asked to provide your refresh token. Your access token and server information will be stored in access.txt and server.txt
3. Run collect_data.py - you have the option to collect your account information, or don't collect account information and collect stock symbol data. You also have the option to collect all data for the symbols in your portfolio.

