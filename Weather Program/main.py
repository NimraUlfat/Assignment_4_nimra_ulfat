import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# Check if the API key is loaded properly
if not api_key:
    print("❌ API key not found. Make sure .env file is set up correctly.")
    exit()  # Exit the program if no API key is found

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        # Successfully received data from the API
        print(f"\nWeather in {data['name']} ({data['sys']['country']}):")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        # Handle errors if API response is not 200 (valid)
        print(f"\nError: {data['message'].capitalize()}")

# Main Function
if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city, api_key)
