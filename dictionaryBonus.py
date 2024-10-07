def input_weather_data(weather_data):
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = input("Enter temperature (°C): ")
    humidity = input("Enter humidity (%): ")
    condition = input("Enter weather condition (e.g., sunny, rainy): ")

    if city not in weather_data:
        weather_data[city] = {}
    
    weather_data[city][date] = {
        'temperature': temperature,
        'humidity': humidity,
        'condition': condition
    }
    print(f"Weather data for {city} on {date} added successfully.")

def query_weather_data(weather_data):
    city = input("Enter city name to query: ")
    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, details in weather_data[city].items():
            print(f"Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print("No data found for the specified city.")

def update_weather_data(weather_data):
    city = input("Enter city name to update: ")
    date = input("Enter date (YYYY-MM-DD) to update: ")
    
    if city in weather_data and date in weather_data[city]:
        temperature = input("Enter new temperature (°C): ")
        humidity = input("Enter new humidity (%): ")
        condition = input("Enter new weather condition (e.g., sunny, rainy): ")
        
        weather_data[city][date] = {
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition
        }
        print(f"Weather data for {city} on {date} updated successfully.")
    else:
        print("No data found for the specified city and date.")

def delete_weather_data(weather_data):
    city = input("Enter city name to delete data: ")
    date = input("Enter date (YYYY-MM-DD) to delete data: ")
    
    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        print(f"Weather data for {city} on {date} deleted successfully.")
        
        if not weather_data[city]:  # Remove city if no data left
            del weather_data[city]
    else:
        print("No data found for the specified city and date.")

def main():
    weather_data = {}
    
    while True:
        print("\nMenu:")
        print("1. Input Weather Data")
        print("2. Query Weather Data")
        print("3. Update Weather Data")
        print("4. Delete Weather Data")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            input_weather_data(weather_data)
        elif choice == '2':
            query_weather_data(weather_data)
        elif choice == '3':
            update_weather_data(weather_data)
        elif choice == '4':
            delete_weather_data(weather_data)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
