import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenWeather API key from the environment variable
api_key = os.getenv('OPEN_WEATHER_API_KEY')

def get_weather_data(lat, lng):
    try:
        # OpenWeatherMap API endpoint with coordinates
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric'

        # Fetch weather data
        response = requests.get(url)
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        precipitation = data.get('rain', {}).get('1h', 0)  # Precipitation in mm/hr

        # Calculate the heat index
        heat_index = calculate_heat_index(temperature, humidity)

        # Categorize heat index and precipitation
        heat_index_category = get_heat_index_category(heat_index)
        precipitation_category = get_precipitation_category(precipitation)

        # Log results
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Heat Index: {heat_index:.2f}°C')
        print(f'Heat Index Category: {heat_index_category}')
        print(f'Precipitation: {precipitation} mm/hr')
        print(f'Precipitation Category: {precipitation_category}')

        return {
            'temperature': temperature,
            'humidity': humidity,
            'heat_index': heat_index,
            'heat_index_category': heat_index_category,
            'precipitation': precipitation,
            'precipitation_category': precipitation_category
        }

    except Exception as error:
        print(f'Error fetching weather data: {error}')

# Function to calculate heat index using temperature and humidity
def calculate_heat_index(T, RH):
    # Heat Index formula from NOAA
    HI = (
        -42.379 +
        2.04901523 * T +
        10.14333127 * RH -
        0.22475541 * T * RH -
        0.00683783 * T * T -
        0.05481717 * RH * RH +
        0.00122874 * T * T * RH +
        0.00085282 * T * RH * RH -
        0.00000199 * T * T * RH * RH
    )
    return HI

# Function to categorize heat index
def get_heat_index_category(heat_index):
    if heat_index < 27:
        return 'Hazardous'
    elif 27 <= heat_index <= 32:
        return 'Caution'
    elif 33 <= heat_index <= 41:
        return 'Extreme Caution'
    elif 42 <= heat_index <= 51:
        return 'Danger'
    elif heat_index >= 52:
        return 'Extreme Danger'

# Function to categorize precipitation
def get_precipitation_category(precipitation):
    if precipitation == 0:
        return 'No Rain'
    elif precipitation <= 2.5:
        return 'Light Rain'
    elif 2.5 < precipitation <= 7.5:
        return 'Moderate Rain'
    elif precipitation > 7.5:
        return 'Heavy Rain'
    return 'No Rain'
