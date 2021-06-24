import requests
import json


def rates(currency = None):
    r = requests.get('https://api.vatcomply.com/rates')

    data = json.loads(r.text)
    return {k: v for k, v in data['rates'].items()}