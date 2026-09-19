# WeatherWear

WeatherWear is a Python application that checks the weather for a city and recommends what to wear based on the forecast.

Instead of simply displaying weather data, WeatherWear turns the forecast into a practical clothing recommendation.

## Features

- Search for any city
- Get today's weather
- Get tomorrow's weather
- View minimum and maximum temperature
- Check probability of rain
- Detect different weather conditions
- Receive clothing recommendations
- Receive additional weather-based notes

## How It Works

The user enters a city.

WeatherWear uses a geocoding service to find the city's coordinates. It then sends those coordinates to a weather API and receives the forecast.

The clothing recommendation system analyses:

- Maximum temperature
- Minimum temperature
- Rain probability
- Weather condition
- Temperature difference between morning and afternoon

It then creates a practical clothing recommendation.

## Project Structure

main.py
The main program that connects everything together.

weather_api.py
Handles location searches and weather API requests.

clothing.py
Contains the clothing recommendation logic.

display.py
Controls how information is displayed in the terminal.

config.py
Stores application configuration.

## Technologies

Python
Open-Meteo API
JSON
HTTP requests
Decision logic

## Running the Application

Open the WeatherWear folder in VS Code.

Run:

python main.py

Enter a city when prompted.

Example:

Johannesburg

## Future Improvements

Possible future versions could include:

- Graphical interface
- Weather icons
- Outfit categories
- School outfit recommendations
- Formal event recommendations
- Activity-based recommendations
- Saved favourite cities
- Seven-day forecasts
- Clothing database
- Mobile version
