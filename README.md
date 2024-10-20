# WeatherPy

WeatherPy is a Python module that fetches current weather data and forecasts from the OpenWeatherMap API. It provides a user-friendly interface to display weather information and includes features like saving weather data for different cities.

## Features

- **Current Weather Retrieval:** Fetch real-time weather data for any city.
- **Weather Forecasting:** Retrieve a 5-day weather forecast with 3-hour intervals.
- **User-Friendly Display:** Present weather information in a readable format.
- **Data Saving:** Save weather data for different cities for later use.

## Dependencies
- requests

## Usage

from weatherpy.weather_retriever import WeatherRetriever

- Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
weather = WeatherRetriever(api_key)

- Get current weather for a city
try:
    city = 'New York'
    current_weather = weather.get_current_weather(city)
    weather.display_weather(current_weather)
    weather.save_weather(city, current_weather)
except Exception as e:
    print(e)

- Get weather forecast for the same city
try:
    forecast_data = weather.get_forecast(city)
    weather.display_forecast(forecast_data)
except Exception as e:
    print(e)

- Load saved weather data
saved_weather = weather.load_saved_weather(city)
if saved_weather:
    print("\nLoaded saved weather data:")
    weather.display_weather(saved_weather)
else:
    print("No saved weather data found for this city.")

## Installation

To install the required dependencies, use the following command:

```bash
pip install requests
