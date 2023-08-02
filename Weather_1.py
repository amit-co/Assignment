import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(city_name, api_key):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Function to get temperature for a specific date from weather data
def get_temperature_for_date(weather_data, date):
    for item in weather_data["list"]:
        if date in item["dt_txt"]:
            return item["main"]["temp"]
    return None

# Function to get wind speed for a specific date from weather data
def get_wind_speed_for_date(weather_data, date):
    for item in weather_data["list"]:
        if date in item["dt_txt"]:
            return item["wind"]["speed"]
    return None

# Function to get pressure for a specific date from weather data
def get_pressure_for_date(weather_data, date):
    for item in weather_data["list"]:
        if date in item["dt_txt"]:
            return item["main"]["pressure"]
    return None

# Main program
def main():
    city_name = "London,us"
    api_key = "b6907d289e10d714a6e88b30761fae22"

    weather_data = get_weather_data(city_name, api_key)

    if not weather_data:
        print("Failed to fetch weather data.")
        return

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = int(input("Enter your choice: "))

        if option == 0:
            print("Exiting program.")
            break

        date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")

        if option == 1:
            temperature = get_temperature_for_date(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("Data not available for the given date.")
        elif option == 2:
            wind_speed = get_wind_speed_for_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} km/h")
            else:
                print("Data not available for the given date.")
        elif option == 3:
            pressure = get_pressure_for_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available for the given date.")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()