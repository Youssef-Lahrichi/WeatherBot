from time import time
import discord
from discord.ext import commands
import OpenWeatherMap

client= commands.Bot(command_prefix='!')


DISCORD_TOKEN = 'discord key here'
WEATHER_TOKEN = 'openweather key here'

@client.event
async def on_ready():
    # print('We have logged in as {0.user}'.format(client))
    pass


@client.command()
async def temp(ctx, cityname='Seattle'):
    temp = OpenWeatherMap.get_temp(WEATHER_TOKEN, cityname)

    await ctx.send(temp)

@client.command()
async def weather(ctx, cityname='Seattle'):
    weather = OpenWeatherMap.get_weather(WEATHER_TOKEN, cityname)

    await ctx.send('http://openweathermap.org/img/wn/{}@2x.png'.format(weather[2]))
    await ctx.send("The current weather is {}, which means: {}".format(weather[0], weather[1]))
    
@client.command()
async def sunrise(ctx, cityname='Seattle'):
    sunrise = OpenWeatherMap.get_sunrise(WEATHER_TOKEN, cityname)

    await ctx.send(sunrise)

@client.command()
async def sunset(ctx, cityname='Seattle'):
    sunset = OpenWeatherMap.get_sunset(WEATHER_TOKEN, cityname)

    await ctx.send(sunset)

@client.command()
async def forecast(ctx, cityname='Seattle'):
    temps, times, icons = OpenWeatherMap.get_forecast(WEATHER_TOKEN, cityname)

    for i in range(8):
        await ctx.send('http://openweathermap.org/img/wn/{}@2x.png'.format(icons[i]))
        await ctx.send("{} {} °F".format(times[i], temps[i]))
        



client.run(DISCORD_TOKEN)