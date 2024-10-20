import requests

class WeatherRetriever:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url_current = 'http://api.openweathermap.org/data/2.5/weather'
        self.api_url_forecast = 'http://api.openweathermap.org/data/2.5/forecast'
        self.saved_weather = {}

    def get_current_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(self.api_url_current, params=params)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            error_message = data.get('message', 'Failed to retrieve weather data')
            raise Exception(f"Error fetching weather data: {error_message}")

    def display_weather(self, weather_data):
        city = weather_data['name']
        country = weather_data['sys']['country']
        weather_description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Weather in {city}, {country}:")
        print(f"{weather_description.capitalize()}")
        print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")

    def get_forecast(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.api_url_forecast, params=params)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            error_message = data.get('message', 'Failed to retrieve forecast data')
            raise Exception(f"Error fetching forecast data: {error_message}")

    def display_forecast(self, forecast_data):
        city = forecast_data['city']['name']
        country = forecast_data['city']['country']
        print(f"\n5-day Forecast for {city}, {country}:")
        for entry in forecast_data['list']:
            timestamp = entry['dt_txt']
            weather_description = entry['weather'][0]['description']
            temp = entry['main']['temp']
            print(f"{timestamp}: {weather_description.capitalize()}, {temp}°C")

    def save_weather(self, city, weather_data):
        self.saved_weather[city] = weather_data

    def load_saved_weather(self, city):
        return self.saved_weather.get(city, None)
