weather_data = {}


def input_weather_data():
    city = input("Enter city name: ").strip().capitalize()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    temperature = input("Enter temperature (°C): ").strip()
    humidity = input("Enter humidity (%): ").strip()
    condition = input("Enter weather condition (e.g., sunny, rainy): ").strip().capitalize()

    
    if city not in weather_data:
        weather_data[city] = {}
    
    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
    print(f"Weather data added for {city} on {date}.\n")


def query_by_city():
    city = input("Enter city name to query: ").strip().capitalize()
    if city in weather_data:
        for date, details in weather_data[city].items():
            print(f"Date: {date}, Temp: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print(f"No data available for {city}.\n")


def update_weather_data():
    city = input("Enter city name to update: ").strip().capitalize()
    if city in weather_data:
        date = input("Enter date to update (YYYY-MM-DD): ").strip()
        if date in weather_data[city]:
            temperature = input("Enter new temperature (°C): ").strip()
            humidity = input("Enter new humidity (%): ").strip()
            condition = input("Enter new weather condition: ").strip().capitalize()
            weather_data[city][date] = {
                "temperature": temperature,
                "humidity": humidity,
                "condition": condition
            }
            print(f"Weather data updated for {city} on {date}.\n")
        else:
            print(f"No data found for {city} on {date}.\n")
    else:
        print(f"No data available for {city}.\n")


def delete_weather_data():
    city = input("Enter city name to delete data from: ").strip().capitalize()
    if city in weather_data:
        date = input("Enter date to delete (YYYY-MM-DD): ").strip()
        if date in weather_data[city]:
            del weather_data[city][date]
            print(f"Weather data deleted for {city} on {date}.\n")
            
        
            if not weather_data[city]:
                del weather_data[city]
                print(f"No more data for {city}, city removed.\n")
        else:
            print(f"No data found for {city} on {date}.\n")
    else:
        print(f"No data available for {city}.\n")


def main():
    while True:
        print("1. Input weather data")
        print("2. Query weather data by city")
        print("3. Update weather data")
        print("4. Delete weather data")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            input_weather_data()
        elif choice == "2":
            query_by_city()
        elif choice == "3":
            update_weather_data()
        elif choice == "4":
            delete_weather_data()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.\n")


main()
