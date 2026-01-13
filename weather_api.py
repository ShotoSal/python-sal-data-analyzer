import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def get_weather(latitude, longitude, days=2):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": days,
        "timezone": "auto"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = get_weather(40.7128, -74.0060, 2)
    print(data["hourly"]["temperature_2m"][:5])
