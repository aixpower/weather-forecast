import os
import sys
import requests


def load_config():
    """Load configuration from environment variables or .env file."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    
    api_key = os.getenv('QWEATHER_API_KEY')
    api_host = os.getenv('QWEATHER_API_HOST')
    
    if not api_key:
        raise ValueError(
            "QWEATHER_API_KEY environment variable is not set. "
            "Please set it or create a .env file with your API key."
        )
    
    if not api_host:
        raise ValueError(
            "QWEATHER_API_HOST environment variable is not set. "
            "Please set it or create a .env file with your custom API host from https://dev.qweather.com/"
        )
    
    return api_key, api_host


def get_location_id(city_name, api_key, api_host):
    """Get the location ID for a given city name."""
    url = f"https://{api_host}/geo/v2/city/lookup"
    params = {
        'location': city_name,
        'key': api_key,
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if 'location' not in data or not data['location']:
        raise ValueError(f"No location found for {city_name}")
    return data['location'][0]['id']


def get_weather_forecast(location_id, api_key, api_host):
    """Get the 7 day weather forecast for a location ID."""
    url = f"https://{api_host}/v7/weather/7d"
    params = {
        'location': location_id,
        'key': api_key,
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()


def main(city_name):
    api_key, api_host = load_config()
    location_id = get_location_id(city_name, api_key, api_host)
    forecast_data = get_weather_forecast(location_id, api_key, api_host)
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
