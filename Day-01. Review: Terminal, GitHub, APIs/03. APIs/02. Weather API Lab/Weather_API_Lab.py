# ******* READ THE README FIRST !!!!!!******* #

"""
scratch pad
https://api.openweathermap.org/data/2.5/weather?q=Dallas&appid=79aec617fecca250341e89201367413a
"""

import requests
# requests is a client library for Python used to make HTTP requests

# API_URL = "https://api.openweathermap.org/data/2.5/weather?q=Dallas&appid=79aec617fecca250341e89201367413a"
# # All caps variable names are used to indicate "constant" variables; we do this as a naming convention

# response = requests.get(API_URL)
# # this expression is making a get request (get information) to the openweather api and then assigning the response to a variable 

# data = response.json()
# # this expression is extracting the JSON response body (data) from the response object

# temp = data['main']['temp']
# print(temp)
# location = data['name']
# print(location)

"""
Make a request to the OpenWeather and get current weather details for location

The user will provide the location as input

Requirements:
    Use OpenWeatherAPI Key
    Requests lirary
    OpenWeather API docs

    ex 1. Prompt user for a location or to quit the program

    ex 2. given user input if the user is to get weather details, ask the user for a location and use the location to make a request to open weather

    ex 3. given user input, if the user input is to quit
    
"""
divider = "***************************************************************************************************************************************"
location = ""


print(divider)
COMMAND = ""
while COMMAND != "q":
    COMMAND = input("Choose [c] for current weather or [q] to quit: ")
    if COMMAND == "c":
        location = input("Where would you like to lookup: ")
        API_KEY = "79aec617fecca250341e89201367413a"
        API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=imperial"
        response = requests.get(API_URL)
        data = response.json()
        temp = data['main']['temp']
        location_name = data['name']
        print(f"{location_name}: {temp}")

print(divider)