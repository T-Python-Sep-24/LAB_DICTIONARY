weatherData = {}

def inputWeather():
    while True:
        city = input("enter city name  or exit :  ")
        if city == "exit":
            break
        date = input("enter date : ")
        temperature = input("enter temperature : ")
        humidity = input("enter humidity : ")
        condition = input("enter weather condition : ")

        
        if city not in weatherData:
            weatherData[city] = {}
        
        weatherData[city][date] = {
            'temperature': int(temperature),
            'humidity': int(humidity),
            'condition': condition
        }

def queryWeather():
    city = input("Enter city name to query: ")
    if city in weatherData:
        print("Weather data for :",city)
        for date in weatherData[city]:
           print("date : {}, temperature : {}, humidity : {} condition : {} ".format(
               date,weatherData[city][date]['temperature'],
               weatherData[city][date]['humidity'],
               weatherData[city][date]['condition'] ))
    else:
        print("No weather data found for ",city)

def updateWeather():
    city = input("enter city name :  ")
    date = input("enter date : ")

    if city in weatherData and date in weatherData[city]:
        temperature = input("enter temperature : ")
        humidity = input("enter humidity : ")
        condition = input("enter weather condition : ")

    if temperature.isdigit() and humidity.isdigit():
        weatherData[city][date] = {
            'temperature': int(temperature),
            'humidity': int(humidity),
            'condition': condition
        }
        print("data update ")
    else:
        print("city or date not found")

def deleteWeather():
   city = input("enter city name to delete data: ")
   date = input("enter date : ")

   if city in weatherData and date in weatherData[city]:
        del weatherData[city][date]
        print(" data deleted ")
        if not weatherData[city]:
            del weatherData[city]
   else:
        print("city or date not found.")

def printall():
    if not weatherData:
        print("no weather data available")
        return
    else:
     for city, dates in weatherData.items():
        print(f"weather data for {city}:")
        for date, details in dates.items():
           print("date : {}, temperature : {}, humidity : {} condition : {} ".format(
               date,weatherData[city][date]['temperature'],
               weatherData[city][date]['humidity'],
               weatherData[city][date]['condition'] ))
        print()  


while True:
    print("1. Input Weather Data")
    print("2. Query by City")
    print("3. Update Weather Data")
    print("4. Delete Weather Data")
    print("5. Print All Weather Data")
    print("6. Exit")
    
    
    selection = input("select an option. (1-6): ")
    
    if selection == '1':
         inputWeather()
    elif selection == '2':
         queryWeather()
    elif selection == '3':
         updateWeather()
    elif selection == '4':
         deleteWeather()
    elif selection == '5':
         printall()
    elif selection == '6':
        print("exiting the program.")
        break

    else:
        print("Selection not recognized. Please choose again.")
