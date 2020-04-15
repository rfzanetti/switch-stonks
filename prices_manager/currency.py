import json
import requests

FIXER_API_BASE_URL = 'http://data.fixer.io/api'
FIXER_API_VERSION = 'latest'


class CurrencyConverter():

    def __init__(self):

        with open('config.json') as config_file:
            config = json.load(config_file)
            self.api_access_key = config['fixer_api_access_key']

        self.rates = self.request_conversion_rates()

    def request_conversion_rates(self):

        url = f'{FIXER_API_BASE_URL}/{FIXER_API_VERSION}?access_key={self.api_access_key}'
        rates = json.loads(requests.get(url).text)['rates']

        return rates

    def get_conversion_rate(self, currency_code, base):

        return self.rates[currency_code] / self.rates[base]
