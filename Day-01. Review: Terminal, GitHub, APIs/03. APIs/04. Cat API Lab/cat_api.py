""" cat_api.py """
import requests

data = requests.get('https://catfact.ninja/breeds', timeout=10)

# print(data.json()['data'][1]['breed'])

# print(data.json()['data'][4]['origin'])


print(type(data.json()['data']))
