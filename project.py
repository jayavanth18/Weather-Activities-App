import requests
import time
from datetime import datetime, timezone, timedelta

# Weather code to description map
WEATHER_CODES = {
    0: "Clear", 1: "Clear", 2: "Cloudy", 3: "Cloudy",
    45: "Fog", 48: "Fog", 51: "Rain", 53: "Rain", 55: "Rain",
    61: "Rain", 63: "Rain", 65: "Rain", 71: "Snow", 73: "Snow",
    75: "Snow", 77: "Snow", 80: "Rain", 81: "Rain", 82: "Rain",
    95: "Thunderstorm", 96: "Thunderstorm", 99: "Thunderstorm"
}

# Activity suggestions based on weather
activity_suggestions = {
    "Clear": ["Go for a walk", "Have a picnic", "Play outdoor sports"],
    "Cloudy": ["Take photographs", "Visit a cafe", "Go on a short hike"],
    "Rain": ["Visit a museum", "Read a book", "Go to a cafe"],
    "Snow": ["Build a snowman", "Go skiing", "Watch a movie indoors"],
    "Fog": ["Visit indoor attractions", "Do indoor workouts", "Bake something warm"],
    "Thunderstorm": ["Stay indoors", "Watch a movie", "Play board games"],
    "Unknown": ["Try a new hobby", "Check out YouTube tutorials"]
}

def get_local_time_utc(longitude):
    try:
        utc_now = datetime.now(timezone.utc)
        offset = int(longitude / 15)
        local_time = utc_now + timedelta(hours=offset)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
    except:
        print("⚠️ Could not fetch accurate local time. Showing UTC.")
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def safe_request(url, params, retries=3, timeout=18):
    for _ in range(retries):
        try:
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            time.sleep(2)
    return None

def get_weather_data(location):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": location, "count": 1}
    geo_response = safe_request(geo_url, geo_params)

    if not geo_response:
        print("❌ Failed to get location coordinates after retries.")
        return None

    geo_data = geo_response.json()
    if not geo_data.get("results"):
        return None

    city_info = geo_data["results"][0]
    lat, lon = city_info["latitude"], city_info["longitude"]
    city_name = city_info["name"]
    country = city_info.get("country", "Unknown")

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    weather_response = safe_request(weather_url, weather_params)
    if not weather_response:
        print("❌ Failed to get weather data after retries.")
        return None

    weather_data = weather_response.json()
    weather = weather_data.get("current_weather", {})
    weather_code = weather.get("weathercode", -1)
    condition = WEATHER_CODES.get(weather_code, "Unknown")

    return {
        "city": city_name,
        "country": country,
        "temperature": weather.get("temperature", "N/A"),
        "wind_speed": weather.get("windspeed", "N/A"),
        "condition": condition,
        "longitude": lon
    }

def suggest_activities(condition):
    return activity_suggestions.get(condition, activity_suggestions["Unknown"])

def display_weather_info(data):
    print(f"\n📍 Location: {data['city']}, {data['country']}")
    print(f"🕒 Local Time: {get_local_time_utc(data['longitude'])}")

    print("\n🌡️ Weather Details:")
    print("+---------------------+----------------+")
    print("| {:<19} | {:<14}|".format("Metric", "Value"))
    print("+---------------------+----------------+")
    print("| {:<19} | {:<14}|".format("Condition", data['condition']))
    print("| {:<19} | {:<14}|".format("Temperature (°C)", data['temperature']))
    print("| {:<19} | {:<14}|".format("Wind Speed (km/h)", data['wind_speed']))
    print("+---------------------+----------------+")

    activities = suggest_activities(data["condition"])
    print("\n🎯 Suggested Activities:")
    for idx, activity in enumerate(activities[:3], 1):
        print(f"  {idx}. {activity}")
    print()

def main():
    print("🌤️ Welcome to the Weather & Activities App 🌤️")
    location = input("Enter the city name: ").strip()

    if not location:
        print("❌ Please enter a valid city name.")
        return

    data = get_weather_data(location)
    if data:
        display_weather_info(data)
    else:
        print("❌ Could not retrieve data for the given location.")

if __name__ == "__main__":
    main()
