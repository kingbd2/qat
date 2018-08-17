# QAT

Questrade API Toolkit. Also, the easiest Q word in Scrabble. You're welcome.

## Getting Started

Create Questrade Personal App at https://www.questrade.com/api and generate refresh token (must have Questrade account).

Run refresh_token.py - you will be asked to provide your refresh token. Your access token and server information will be stored in access.txt and server.txt

Run collect_data.py - you have the option to collect your account information, or don't collect account information and collect stock symbol data. You also have the option to collect all data for the symbols in your portfolio.

### Prerequisites

* Python 3.6

### Installing

Clone this repository and run pipenv install.

```
pipenv install
```

## Built With

* Python 3.6
* Requests

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

0.1

## Authors

* **Brian King** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
