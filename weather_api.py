import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from config import GEOCODING_URL, WEATHER_URL, FORECAST_DAYS


def fetch_json(url, params):
    query_string = urlencode(params)
    full_url = f"{url}?{query_string}"

    request = Request(
        full_url,
        headers={
            "User-Agent": "WeatherWear/1.0"
        }
    )

    try:
        with urlopen(request, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))

    except HTTPError as error:
        raise RuntimeError(f"Weather service returned error {error.code}.")

    except URLError:
        raise RuntimeError("Could not connect to the weather service.")

    except TimeoutError:
        raise RuntimeError("The weather request timed out.")


def find_city(city):
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    data = fetch_json(GEOCODING_URL, params)

    results = data.get("results", [])

    if not results:
        raise ValueError(f"Could not find a city called '{city}'.")

    location = results[0]

    return {
        "name": location.get("name", city),
        "country": location.get("country", "Unknown"),
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timezone": location.get("timezone", "Unknown")
    }


def get_forecast(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ",".join([
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max"
        ]),
        "timezone": "auto",
        "forecast_days": FORECAST_DAYS
    }

    data = fetch_json(WEATHER_URL, params)

    daily = data.get("daily")

    if not daily:
        raise RuntimeError("No forecast data was returned.")

    forecast = []

    for index, date in enumerate(daily["time"]):
        forecast.append({
            "date": date,
            "weather_code": daily["weather_code"][index],
            "max_temperature": daily["temperature_2m_max"][index],
            "min_temperature": daily["temperature_2m_min"][index],
            "rain_probability": daily["precipitation_probability_max"][index]
        })

    return forecast