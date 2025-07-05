# backend/tools/weather.py
import requests
import os

def get_weather(city: str) -> str:
    """
    Fetch current weather for a city using OpenWeather API.

    Args:
        city (str): City name

    Returns:
        str: Description of weather + temperature
    """
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return f"{data['weather'][0]['description']}, Temp: {data['main']['temp']}\u00b0C"