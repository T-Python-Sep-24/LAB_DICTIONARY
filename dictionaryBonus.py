# Functions for adding, showing, updating, removing for the main weather list
import datetime

weather_data = {
    "jeddah": {
        datetime.date(2024, 10, 6): {
            "temp": 22.5,
            "humidity": 65,
            "condition": "partly cloudy"
        },
        datetime.date(2024, 10, 5): {
            "temp": 25,
            "humidity": 45,
            "condition": "sunny"
        }
    },

    "riyadh": {
        datetime.date(2001,11,25):{
            "temp": "45",
            "humidity": "9",
            "condition": "sunny"
        }
    },
}


def valDate(date_string):

    return datetime.datetime.strptime(date_string, "%d-%m-%Y").date()
# TODO function to add to the list
def add_weather_data(weatherList):
    city = input("Enter City name: ")
    date_string = input("Enter the Date (DD-MM-YYYY): ")
    temp = input("Enter the Temperature: ")
    humidity = input("Enter the humidity: ")
    condition = input("Enter the Weather Condition: (ie. sunny, rainy): ")

    validDate = valDate(date_string)


    if city not in weatherList:
        weatherList[city] = {}

    weatherList[city][validDate] = {
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }
    print(f"{city} weather data is successfully added")
    # return weatherList


# TODO query by the city
def query_city_data(weatherList):
    city = input("Enter City Name to show its data: ")
    if city in weatherList:
        print(f"{city.upper()} Weather Data: ")

        for date, data in weatherList[city].items():

            print(f">> Date: {date}, Temperature: {data['temp']}°C, "
                  f"Humidity: {data['humidity']}%, Condition: {data['condition']}")

    elif not city in weatherList:
        return f"!!! No Records Found of the City {city}"

# TODO function to update the list
def update_city_data(weatherList:dict):

    city = input("Enter City to UPDATE: ")
    date_string = input("Enter date to UPDATE (DD-MM-YYYY): ").strip()

    validDate = valDate(date_string)

    if city in weatherList and validDate in weatherList[city]:

        temp = input("Enter new temperature or press Enter to keep current: ").strip()
        humidity = input("Enter new humidity or press Enter to keep current: ").strip()
        condition = input("Enter new weather condition or press Enter to keep current: ").strip()


        if len(temp) > 0:
            weatherList[city][validDate]["temp"] = temp
        if len(humidity) > 0:
            weatherList[city][validDate]["humidity"] = humidity
        if len(condition) > 0:
            weatherList[city][validDate]["condition"] = condition
        return f"Weather data of {city} is updated successfully"

    else:

        return f"The City {city} has no records yed"



# TODO function to delete from the list

def deleteCity(weatherList: dict):
    city = input("Enter City to remove: ")
    date_string = input("Enter date (DD-MM-YYYY): ")
    validDate = valDate(date_string)

    if city in weatherList and validDate in weatherList[city]:
        toDelete = weatherList[city].pop(validDate)
    return f" Record of {city} on {date_string} is deleted successfully"

# User Interactions TODO

print("-"*31)
print("    Welcome to WeatherWise    ")


while True:

    print("-"*31)
    print("1. Enter new City weather data \n2. Search City weather data \n3. Update city data\n4. Delete city data \n5. Exit")
    print("="*31)

    choice = input(">>> Enter Your Choice: ")
    if choice == "1":
        print(add_weather_data(weather_data))

    elif choice == "2":
        # todo edit print
        query_city_data(weather_data)
    elif choice == "3":
        print(update_city_data(weather_data))
    elif choice == "4":
        print(deleteCity(weather_data))
    elif choice == "5":
        print("Thank You For Using My Application, See Your Later")
        break
    else:
        print("Please Choose from the list above.")
