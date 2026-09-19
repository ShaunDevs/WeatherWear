from clothing import get_clothing_recommendation, get_weather_description


def print_header():
    print()
    print("=" * 48)
    print("                 WEATHERWEAR")
    print("             Dress for the weather.")
    print("=" * 48)


def print_forecast(day_name, forecast):
    description = get_weather_description(forecast["weather_code"])
    recommendation = get_clothing_recommendation(forecast)

    print()
    print(day_name.upper())
    print("-" * 48)

    print(f"Condition: {description}")
    print(
        f"Temperature: "
        f"{forecast['min_temperature']:.0f}°C - "
        f"{forecast['max_temperature']:.0f}°C"
    )
    print(f"Rain chance: {forecast['rain_probability']}%")

    print()
    print("WHAT TO WEAR")
    print("-" * 48)

    for item in recommendation["clothes"]:
        print(f"- {item}")

    if recommendation["notes"]:
        print()
        print("NOTE")

        for note in recommendation["notes"]:
            print(f"- {note}")


def print_location(location):
    print()
    print(
        f"Location: {location['name']}, "
        f"{location['country']}"
    )
    print(f"Timezone: {location['timezone']}")