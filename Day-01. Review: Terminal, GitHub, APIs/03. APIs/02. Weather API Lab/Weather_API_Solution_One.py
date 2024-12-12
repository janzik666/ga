""" weather-api-solution.py """

import requests

""" This is my API key. Generally it is bad practice to
 store APIKeys directly in code, so this is just for demo purposes """
API_KEY = "79aec617fecca250341e89201367413a"

command = ""
while command != "q":
    command = input(
        "Choose [c] for current weather, [f] for a forecast, and [q] to quit.")
    if command == "c":
        location = input(
            "What location would you like the current weather for: ")
        data = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}')
        kelvin_temp = data.json()['main']['temp']
        print(
            f'The weather in {location} is {kelvin_temp} Kelvin" using the location and temperature result')
    if (command == "f"):
        location = input("What location would you like a forecast for?")
        count = input("How many days would you like (choose up to 16)")
        data = requests.get(
            f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}&cnt={count}')
        list_of_forecasts = data.json()['list']

        for forecast in list_of_forecasts:
            datetime_text = forecast['dt_txt']
            temp = forecast['main']['temp']
            print(
                f'The temperature in {location} on {datetime_text} is {temp} Kelvin.')
