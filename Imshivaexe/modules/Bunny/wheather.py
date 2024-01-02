from pyrogram import Client, filters
import requests
from config import HANDLER as hl
from Imshivaexe import Bunny
from config import WEATHER_API

api_key = WEATHER_API

@Bunny.on_message(filters.command("weather", hl) & filters.me)
async def get_weather_info(client, message):
    location = message.text.split(' ', 1)
    if len(location) > 1:
        city = location[1]
        weather_info = fetch_weather_info(city)
        await message.edit(weather_info)
    else:
        await message.edit("`Please specify the city for the weather information...`")

def fetch_weather_info(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_info = f"**Weather in {city}~**\n\n {description}, \n\n๏** Temperature**: {temperature}°C, \n\n๏** Humidity**: {humidity}%, \n\n๏** Wind Speed:** {wind_speed} m/s"
            return weather_info
        else:
            return "`Failed to fetch weather information for the specified city.`"
    except Exception as e:
        return "`An error occurred while fetching weather information.`"
