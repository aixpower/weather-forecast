import os
import sys
import requests

API_KEY = '75edd03acdf84276a93daec60f60bdf8'
API_HOST = 'mj4d92etey.re.qweatherapi.com'


def get_location_id(city_name):
    """Get the location ID for a given city name."""
    url = f"https://{API_HOST}/geo/v2/city/lookup"
    params = {
        'location': city_name,
        'key': API_KEY,
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if 'location' not in data or not data['location']:
        raise ValueError(f"No location found for {city_name}")
    return data['location'][0]['id']


def get_weather_forecast(location_id):
    """Get the 7 day weather forecast for a location ID."""
    url = f"https://{API_HOST}/v7/weather/7d"
    params = {
        'location': location_id,
        'key': API_KEY,
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def main(city_name):
    location_id = get_location_id(city_name)
    forecast_data = get_weather_forecast(location_id)
    daily_list = forecast_data.get('daily', [])
    if not daily_list:
        print(f"No forecast data for {city_name}")
        return
    print(f"7-Day Weather Forecast for {city_name}:")
    for day in daily_list:
        date = day.get('fxDate')
        text_day = day.get('textDay')
        temp_max = day.get('tempMax')
        temp_min = day.get('tempMin')
        print(f"{date}: {text_day}, {temp_min}-{temp_max}°C")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python qweather_forecast.py <city_name>")
        sys.exit(1)
    city = sys.argv[1]
    main(city)
