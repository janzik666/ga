""" weather-api-solution.py """

import requests

COMMAND = ""
BASE_URL = "http://api.openweathermap.org"

# This is my API key. Generally it is bad practice to
# store APIKeys directly in code, so this is just for demo purposes
API_KEY = "79aec617fecca250341e89201367413a"


def convert_city_name_to_lat_long(city_name):
    """ Convert city name to latitude and longitude """
    city_name_url = f"{BASE_URL}/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    geo_result = requests.get(city_name_url, timeout=10)
    parsed_geo_result = geo_result.json()
    lat = parsed_geo_result[0]["lat"]
    lon = parsed_geo_result[0]["lon"]
    return [lat, lon]


# We're removing the option for the user to ask for a forecast
# Since that functionality is now a premium feature in our API
while COMMAND != "q":
    COMMAND = input(
        "Choose [c] for current weather, [f] for forecast, and [q] to quit. ")
    if COMMAND == "c":
        location = input("What city would you like the current weather for: ")

        lat_long = convert_city_name_to_lat_long(location)
        url = f"{BASE_URL}/data/2.5/weather?lat={lat_long[0]}&lon={lat_long[1]}&appid={API_KEY}"
        weather_result = requests.get(url, timeout=10)
        parsed_weather_result = weather_result.json()
        temperature = parsed_weather_result["main"]["temp"]
        temperature_in_fahrenheit = (temperature - 273.15) * 9/5 + 32
        print(
            f"The weather in {location} is {temperature_in_fahrenheit} degrees fahrenheit ")
        i = 0
        while i < temperature_in_fahrenheit:
            print("+", end='')
            i += 5
        while i < 120:
            print("-", end='')
            i += 5
        print(f" {int(temperature_in_fahrenheit)}\n")
    if COMMAND == "f":
        location = input("What location would you like a forecast for? ")
        count = input("How many forecasts would you like? ")
        data = requests.get(
            f'{BASE_URL}/data/2.5/forecast?q={location}&appid={API_KEY}&cnt={count}',
            timeout=10)
        list_of_forecasts = data.json()['list']

        for forecast in list_of_forecasts:
            datetime_text = forecast['dt_txt']
            temp = forecast['main']['temp']
            temperature_in_fahrenheit = (temp - 273.15) * 9/5 + 32
            print(
                f'The temperature in {location} on {datetime_text} will be {temperature_in_fahrenheit} degrees fahrenheit.')
