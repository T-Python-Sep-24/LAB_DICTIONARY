def add_weather_data(weather_data):
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature (°C): ")
    humidity = input("Enter humidity (%): ")
    condition = input("Enter weather condition (e.g., sunny, rainy): ")
    if not city or not date or not temperature.isdigit() or not humidity.isdigit() or not condition:
        print("Invalid input. Please try again.")
        return
    if city not in weather_data:
        weather_data[city] = {}
    weather_data[city][date] = {
        'temperature': float(temperature),
        'humidity': float(humidity),
        'condition': condition
    }
    print(f"Weather data for {city} on {date} added successfully.")
def query_weather_data(weather_data):
    city = input("Enter city name to query: ")
    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, details in weather_data[city].items():
            print(f"  Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print(f"No data found for {city}.")
def update_weather_data(weather_data):
    city = input("Enter city name to update: ")
    date = input("Enter date (YYYY-MM-DD) to update: ")
    if city in weather_data and date in weather_data[city]:
        temperature = input("Enter new temperature (°C): ")
        humidity = input("Enter new humidity (%): ")
        condition = input("Enter new weather condition: ")
        if temperature.isdigit() and humidity.isdigit() and condition:
            weather_data[city][date]['temperature'] = float(temperature)
            weather_data[city][date]['humidity'] = float(humidity)
            weather_data[city][date]['condition'] = condition
            print(f"Weather data for {city} on {date} updated successfully.")
        else:
            print("Invalid input. Please try again.")
    else:
        print(f"No data found for {city} on {date}.")
def delete_weather_data(weather_data):
    city = input("Enter city name to delete data from: ")
    date = input("Enter date (YYYY-MM-DD) to delete: ")
    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        print(f"Weather data for {city} on {date} deleted successfully.")
        if not weather_data[city]:  # Remove the city if no data left
            del weather_data[city]
    else:
        print(f"No data found for {city} on {date}.")
def main():
    weather_data = {}
    while True:
        print("\nWeather Data Menu:")
        print("1. Add Weather Data")
        print("2. Query Weather Data")
        print("3. Update Weather Data")
        print("4. Delete Weather Data")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_weather_data(weather_data)
        elif choice == '2':
            query_weather_data(weather_data)
        elif choice == '3':
            update_weather_data(weather_data)
        elif choice == '4':
            delete_weather_data(weather_data)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()