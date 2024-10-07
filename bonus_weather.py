"""
program that aggregates weather data for different cities 
and provides weather data based on user queries.
"""
weatherDict = {}

def inputWeatherData(city):
    '''
    Get city from user

    Args:
        city (str): city name
    Returns:
        None: no returns value
    '''
    # validate user input is text
    while True:
        if city.isalpha():
            break
        print("This is invalid name. Use only city names")
        # press any key to continue
        input("")
        city = input("Type City Name: ")
    
    # create dict with city name
    weatherDict[city] = {}
    weatherDict[city]["date"] = input("date for example (10-09-2024): ")
    weatherDict[city]["temperature"] = float(input("temperature in Celsius for example (29): "))
    weatherDict[city]["humidity"] = int(input("humidity in percentage for example (80): " ))
    weatherDict[city]["weatherCondition"] = input("weather condition for example (sunny, or cloudy): ")


def queryCity(city: str):
    '''
    query the weather data by city name

    Args:
        city (str): city name

    Returns:
        None: no returns value
    '''
    for key, cityData in weatherDict.items():
        if city.lower() == key.lower():
            # print weather data
            print(f"--- Weather Data for {city} ----")
            for dataKey, dataValue in cityData.items():
                print(f"{dataKey}: {dataValue}")
            break
    else:
        print("City is not Found")
            
def updateCityData(city: str):
    '''
    update the weather data by city name

    Args:
        city (str): city name

    Returns:
        None: no returns value
    '''
    # check if city existed
    for key in weatherDict.keys():
        if city.lower() == key.lower():
            print(f"City data is found. Please update the data")
            weatherDict[city]["date"] = input("date for example (10-09-2024): ")
            weatherDict[city]["temperature"] = float(input("temperature in Celsius for example (29): "))
            weatherDict[city]["humidity"] = int(input("humidity in percentage for example (80): " ))
            weatherDict[city]["weatherCondition"] = input("weather condition for example (sunny, or cloudy): ")
            break
    else:
        print(f"City data is not found. Please enter the new city data")
        inputWeatherData(city)


def deleteCityData(city: str):
    '''
    delete the weather data of a city

    Args:
        city (str): city name

    Returns:
        None: no returns value
    '''
    for key in weatherDict.keys():
        print(f"{city} {key}")
        if city.lower() == key.lower():
            print(f"{city} data is found and deleted")
            del weatherDict[key]
            break
    else:
        print(f"{city} data is not found. Nothing is deleted")


print("*** Welcome to weather program ***")
while True:
    print("Pick: \n1: to input weather date\n2: to query weather by city name\n3: to update city data\n4: to delete city data\n5: to exit ")
    pick: int = input("Enter: ")
    if pick == "1":
        print("--- Inputing Weather Data ---")
        cityName = input("Type City Name: ")
        inputWeatherData(cityName)
    elif pick == "2":
        print("--- Querying Weather by City Name ---")
        cityName = input("Query by City name: ")
        queryCity(cityName)
    elif pick == "3":
        print("--- Updating City Data ---")
        cityName = input("Type City name: ")
        updateCityData(cityName)
    elif pick == "4":
        print("--- Deleting City Data ---")
        cityName = input("Type City name: ")
        deleteCityData(cityName)
    else:
        break
    input("")