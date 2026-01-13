import requests

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_hourly_temperature(lat, lon, timezone="America/New_York"):
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "forecast_days": 1,
        "timezone": timezone
    }

    response = requests.get(OPEN_METEO_URL, params=params)
    response.raise_for_status()

    data = response.json()

    hourly = data.get("hourly", {})
    times = hourly.get("time", [])
    temperatures = hourly.get("temperature_2m", [])

    return times, temperatures
