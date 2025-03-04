import requests
import json

# Replace 'your_api_key_here' with your actual OpenWeatherMap API key
API_KEY = '3372068375f84f1f56a1f76b3428e337'
def get_weather_data(city_name):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    
    # Make a GET request to the API
    response = requests.get(base_url)

    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Extract relevant weather data
        main = data['main']
        weather_description = data['weather'][0]['description']
        temperature = main['temp']  # Temperature in Kelvin
        temperature_celsius = temperature - 273.15  # Convert to Celsius
        
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature_celsius:.2f}°C")
    else:
        print("Error fetching weather data. Please check your city name and API key.")

# Example usage
city = input("Enter the city name: ")
get_weather_data(city)