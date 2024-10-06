weather= {}
def input_weather_data():
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature (°C): ")
    humidity = input("Enter humidity (%): ")
    condition = input("Enter weather condition (e.g., sunny, rainy): ")

    if not city or not date or not temperature.isdigit() or not humidity.isdigit() or not condition:
        print("Invalid input. Please enter valid data.")
        return
    if city not in weather:
        weather[city]= {}
        weather[city][date] = {
        "temperature": int(temperature),
        "humidity": int(humidity),
        "condition": condition
    }
def query_weather ():
    city = input("Enter the city name: ")
    if city in weather:
        print(f"Weather data for {city}:")
        for date, details in weather[city].items():
            print(f"Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print(f"No weather data found for city: {city}")
def update_weather():
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")

    if city in weather:
        temperature=input("Temperature:")
        humidity = input("humidity (%): ")
        condition = input("Enter weather condition (e.g., sunny, rainy): ")

        weather[city][date] = {
        "temperature": int(temperature),
        "humidity": int(humidity),
        "condition": condition
    }
        for date, details in weather[city].items():
            print(f"Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print(f"No weather data found for city: {city}")
def delete_weather():
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")

    if city in weather and date in weather[city]:
        del weather[city][date]
    else:
        print(f"No data found for {city} on {date}.")

    
def main():
    while True:
        print("\nWeather Data Program")
        print("1. Input Weather Data")
        print("2. Query Weather Data by City")
        print("3. Update Weather Data")
        print("4. Delete Weather Data")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            input_weather_data()
        elif choice == '2':
            query_weather()
        elif choice == '3':
            update_weather()
        elif choice == '4':
            delete_weather()
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()
