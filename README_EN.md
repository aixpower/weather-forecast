# QWeather Forecast

A city weather forecast query tool based on QWeather API, supporting 7-day weather forecasts for cities worldwide.

[中文版](./README.md)

## Features

- 🌍 **Global City Search** - Support for Chinese and English city name search
- 📅 **7-Day Weather Forecast** - Get weather information for the coming week
- 🌡️ **Detailed Weather Data** - Includes weather conditions, high and low temperatures
- 🚀 **Easy to Use** - Single command line query

## Installation

This project depends on the `requests` library, with optional `python-dotenv` for loading environment variables:

```bash
pip install requests python-dotenv
```

## Configuration

### 1. Get API Credentials

Visit [QWeather Development Platform](https://dev.qweather.com/) to register an account and create a project to obtain:
- API Key
- Custom API Host

### 2. Configure Environment Variables

There are two ways to configure:

#### Method 1: Using .env file (Recommended)

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` file and fill in your API key and custom API Host:

```env
QWEATHER_API_KEY=your_actual_api_key_here
QWEATHER_API_HOST=your_custom_api_host_here
```

#### Method 2: Set Environment Variables

Windows:
```cmd
set QWEATHER_API_KEY=your_actual_api_key_here
set QWEATHER_API_HOST=your_custom_api_host_here
```

Linux/Mac:
```bash
export QWEATHER_API_KEY=your_actual_api_key_here
export QWEATHER_API_HOST=your_custom_api_host_here
```

## Usage

Run the script with a city name as parameter:

```bash
python qweather_forecast.py <city_name>
```

### Examples

Query Beijing weather:

```bash
python qweather_forecast.py beijing
```

Or using Chinese:

```bash
python qweather_forecast.py 北京
```

Query other cities:

```bash
python qweather_forecast.py shanghai
python qweather_forecast.py 深圳
```

### Output Example

```
7-Day Weather Forecast for beijing:
2026-05-05: 晴, 17-29°C
2026-05-06: 多云, 13-26°C
2026-05-07: 晴, 10-24°C
2026-05-08: 晴, 12-25°C
2026-05-09: 晴, 15-27°C
2026-05-10: 多云, 17-30°C
2026-05-11: 多云, 18-29°C
```

## Project Structure

```
codex/
├── qweather_forecast.py    # Main program script
├── .env.example            # Environment variable configuration template
├── .gitignore              # Git ignore file configuration
├── README.md               # Project documentation (Chinese)
├── README_EN.md            # Project documentation (English)
└── LICENSE                 # MIT License
```

## QWeather Pricing

QWeather development service uses pay-as-you-go pricing with free monthly quota.

### Weather and Basic Services

Includes: Weather Forecast, Minute Forecast, Alerts, Weather Indices, Air Quality, Time Machine, GeoAPI, Astronomy, Console API

| Monthly Requests | Price per Request |
|---|---|
| 0~50,000 | **Free** |
| Next 950,000 | CNY 0.0007 |
| Next 4,000,000 | CNY 0.0005 |
| Next 5,000,000 | CNY 0.00035 |
| Next 40,000,000 | CNY 0.00015 |
| Next 50,000,000 | CNY 0.0001 |
| Over 100,000,000 | Contact Us |

### Other Services

- **Typhoon and Ocean**: 0~1,000,000 requests, CNY 0.003/request
- **Solar Radiation**: 0~100,000 requests, CNY 0.3/request

For detailed pricing, see: [QWeather Pricing Page](https://dev.qweather.com/docs/finance/pricing/)

## Technical Notes

### API Endpoints

- **City Lookup**: `/geo/v2/city/lookup` - Search city and get Location ID
- **Weather Forecast**: `/v7/weather/7d` - Get 7-day weather forecast

### Workflow

1. Query Location ID by city name
2. Query weather forecast data using Location ID
3. Format and output weather information

## License

MIT License - See [LICENSE](LICENSE) file for details

## Security Notes

- ⚠️ **Never commit `.env` file to Git** - It contains your API keys
- `.gitignore` is configured to automatically ignore `.env` files
- To use your own API credentials, visit [QWeather Development Platform](https://dev.qweather.com/) to register
- Copy `.env.example` to `.env` and fill in your credentials
