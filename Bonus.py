def input_weather_data():
    """Function to input weather data and store it in a nested dictionary."""
    weather_data = {}
    
    while True:
        city = input("Enter city name (or type 'exit' to finish): ")
        if city.lower() == 'exit':
            break
            
        date = input("Enter date (YYYY-MM-DD): ")
        temperature = input("Enter temperature (°C): ")
        humidity = input("Enter humidity (%): ")
        condition = input("Enter weather condition (e.g., sunny, rainy, cloudy, windy): ")

        # Store data in the nested dictionary
        if city not in weather_data:
            weather_data[city] = {}
        
        weather_data[city][date] = {
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition
        }
    
    return weather_data

def query_weather_data(weather_data):
    """Function to query weather data by city name."""
    city = input("Enter city name to query: ")
    
    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, details in weather_data[city].items():
            print(f"Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print(f"No weather data found for {city}.")

def update_weather_data(weather_data):
    """Function to update existing weather data for a specific city and date."""
    city = input("Enter city name to update: ")
    date = input("Enter date of the record to update (YYYY-MM-DD): ")
    
    if city in weather_data and date in weather_data[city]:
        temperature = input("Enter new temperature (°C): ")
        humidity = input("Enter new humidity (%): ")
        condition = input("Enter new weather condition (e.g., sunny, rainy): ")
        
        weather_data[city][date] = {
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition
        }
        print("Weather data updated successfully.")
    else:
        print(f"No data found for {city} on {date}.")

def delete_weather_data(weather_data):
    """Function to delete weather data for a specific city and date."""
    city = input("Enter city name to delete data from: ")
    date = input("Enter date of the record to delete (YYYY-MM-DD): ")
    
    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]
        print("Weather data deleted successfully.")
    else:
        print(f"No data found for {city} on {date}.")

def main():
    weather_data = input_weather_data()
    
    while True:
        print("\nOptions:")
        print("1. Query weather data by city")
        print("2. Update weather data")
        print("3. Delete weather data")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            query_weather_data(weather_data)
        elif choice == '2':
            update_weather_data(weather_data)
        elif choice == '3':
            delete_weather_data(weather_data)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
