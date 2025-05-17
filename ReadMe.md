![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)


# Weather & Activities App 🌤️

#### Video Demo:  [Watch the Demo](https://youtu.be/h_1Ll4w68Gs)

#### Description:
The Weather & Activities App is a Python-based command-line tool that helps users check current weather and receive personalized activity suggestions based on real-time conditions. By entering a city name, the app fetches weather data using the Open-Meteo API and approximates the local time using a simple mathematical formula derived from longitude. This makes it easy for users anywhere in the world to stay informed and entertained.

This project helped me gain hands-on experience working with REST APIs, parsing JSON data, writing modular functions, and designing a user-friendly CLI application. It also introduced me to basic time zone calculations and error handling techniques for real-world scenarios like timeouts or API failures.

The app is designed to be both lightweight and educational — perfect for Python beginners or anyone interested in combining weather data with personalized activity recommendations. It’s also structured for testability and clarity, making it a solid example of beginner-to-intermediate Python programming.

## Features
- Uses Open-Meteo's Geocoding & Weather APIs
- Maps weather codes to simplified conditions like "Clear", "Rain", "Snow"
- Suggests indoor or outdoor activities based on the weather
- Approximates local time using the formula: `longitude / 15`

## Project Structure
- `project.py`: Main program containing all functions and the main entry point
- `test_project.py`: Tests for core functions (`suggest_activities`, `get_local_time_utc`, and `WEATHER_CODES`)
- `requirements.txt`: Lists external Python dependencies (`requests`)

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the app:
   python project.py
