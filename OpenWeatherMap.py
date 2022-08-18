from isort import api
import requests
import math
import datetime

from sqlalchemy import desc

API_KEY = '806dffe16690200899fd89cb5ea09bbe'

def weather_api_call(API_KEY, city='Seattle'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    return requests.get(url).json()

def get_temp(API_KEY, city='Seattle'):

    response = weather_api_call(API_KEY, city)

    print(response)

    temp = response['main']['temp']
    temp = math.floor((temp * 1.8) - 459.67)  # Convert to °F

    feels_like = response['main']['feels_like']
    feels_like = math.floor((feels_like * 1.8) - 459.67)  # Convert to °F

    humidity = response['main']['humidity']
    
    # return 'testing'
    return {
        'Temperature (°F)': temp,
        'Feels Like (°F)': feels_like,
        'Humidity (%)': humidity,
    }

def get_weather(API_KEY, city='Seattle'):

    response = weather_api_call(API_KEY, city)

    weather = response['weather'][0]['main']
    desc = response['weather'][0]['description']
    icon_code = response['weather'][0]['icon']

    return [weather, desc, icon_code]

def get_sunrise(API_KEY, city='Seattle'):

    response = weather_api_call(API_KEY, city)

    sunrise = response['sys']['sunrise']
    timezone = response['timezone']

    return '{} Sunrise: {}'.format(city, datetime.datetime.utcfromtimestamp(sunrise + timezone).strftime('%m-%d-%Y %I:%M %p'))

def get_sunset(API_KEY, city='Seattle'):

    response = weather_api_call(API_KEY, city)

    sunset = response['sys']['sunset']
    timezone = response['timezone']

    return '{} Sunset: {}'.format(city, datetime.datetime.utcfromtimestamp(sunset + timezone).strftime('%m-%d-%Y %I:%M %p'))

def get_forecast(API_KEY, city='Seattle'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"

    response = requests.get(url).json()

    icons, temps, times = [], [], []
    for i in range(8):
        temps.append(math.floor((response['list'][i]['main']['temp'] * 1.8) - 459.67))

        times.append(response['list'][i]['dt_txt'].split()[1])

        icons.append(response['list'][i]['weather'][0]['icon'])
    
    return temps, times, icons


if __name__ == "__main__":
    print(get_forecast(API_KEY, 'Seattle'))