import time
from annotation.utils.weather import get_weather_data


def calculate_accessibility_score():
    while True:
        print("Calculating accessibility score...")

        latitude = 10.327653161715238
        longitude = 123.94290770399293

        get_weather_data(latitude, longitude)

        time.sleep(60*30)
