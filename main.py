from weather_api import find_city, get_forecast
from display import print_header, print_location, print_forecast


def main():
    print_header()

    city = input("\nEnter a city: ").strip()

    if not city:
        print("\nPlease enter a city.")
        return

    try:
        print("\nFinding location...")

        location = find_city(city)

        print("Getting weather forecast...")

        forecast = get_forecast(
            location["latitude"],
            location["longitude"]
        )

        print_location(location)

        if len(forecast) >= 1:
            print_forecast("Today", forecast[0])

        if len(forecast) >= 2:
            print_forecast("Tomorrow", forecast[1])

        print()
        print("=" * 48)
        print("WeatherWear recommendation complete.")
        print("=" * 48)

    except ValueError as error:
        print(f"\nError: {error}")

    except RuntimeError as error:
        print(f"\nError: {error}")

    except KeyboardInterrupt:
        print("\n\nWeatherWear closed.")


if __name__ == "__main__":
    main()