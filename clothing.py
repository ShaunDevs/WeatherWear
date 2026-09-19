WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    56: "Light freezing drizzle",
    57: "Heavy freezing drizzle",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Light snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Light snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail"
}


def get_weather_description(weather_code):
    return WEATHER_CODES.get(weather_code, "Unknown conditions")


def get_clothing_recommendation(forecast):
    max_temp = forecast["max_temperature"]
    min_temp = forecast["min_temperature"]
    rain_probability = forecast["rain_probability"]
    weather_code = forecast["weather_code"]

    clothes = []
    notes = []

    if max_temp >= 28:
        clothes.extend([
            "T-shirt",
            "Shorts or lightweight trousers",
            "Breathable shoes"
        ])

    elif max_temp >= 22:
        clothes.extend([
            "T-shirt",
            "Jeans, chinos or lightweight trousers",
            "Sneakers"
        ])

    elif max_temp >= 16:
        clothes.extend([
            "Long-sleeve shirt or T-shirt",
            "Jeans or trousers",
            "Sneakers"
        ])

    elif max_temp >= 10:
        clothes.extend([
            "Warm jacket",
            "Long trousers",
            "Closed shoes"
        ])

    else:
        clothes.extend([
            "Heavy jacket",
            "Warm layers",
            "Long trousers",
            "Warm closed shoes"
        ])

    if min_temp <= 12 and max_temp > 16:
        clothes.append("Light jacket for the morning and evening")

    if rain_probability >= 50:
        clothes.append("Umbrella")
        clothes.append("Rain jacket")

    elif rain_probability >= 30:
        clothes.append("Consider carrying an umbrella")

    if weather_code >= 95:
        notes.append("Thunderstorms are possible, so avoid open footwear.")

    if weather_code in [45, 48]:
        notes.append("Fog is possible, so visibility may be reduced.")

    if max_temp - min_temp >= 10:
        notes.append("There is a large temperature change during the day. Layers are a good idea.")

    return {
        "clothes": clothes,
        "notes": notes
    }