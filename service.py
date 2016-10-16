# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
import json

API_KEY = 'YOUR_API_TRADE_GOV_ADMIN_KEY_HERE'

URL = "https://api.trade.gov/v1/i92_entries/freshen.json?api_key=" + API_KEY


def handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    try:
        response = requests.get(URL)
        print(response.text)
        return response.text
    except Exception as e:
        print(e)
        raise e
