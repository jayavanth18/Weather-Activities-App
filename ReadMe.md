# Weather & Activities App 🌤️

## Overview
This Python app allows users to:
- Enter a city name
- View current weather (using Open-Meteo API)
- See local time (approximated by longitude)
- Get personalized activity suggestions based on the weather

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
