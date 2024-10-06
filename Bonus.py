#Function for storing data into dictionary 
def weatherDictAdd():
    '''
    This function prompt user to enter city weather data as args and stores it in nested dictionariesa after validating the info
    '''
    weatherInfo = {}
    while True:
        city: str = input("Enter the city's name: ")
        date: str = input("Enter the date (dd-mm-yyyy): ")
        temprature: str = input("Enter the temprature (C): ")
        humidity: str = input("Enter the humidity (%): ")
        weatherCondition: str = input("Enter the weather condition: ")
        if city == " " or date == " " or temprature == " " or humidity == " " or weatherCondition == " ":
            print("Please fill all fields!")
            continue
        if not date.replace("-", "").isdigit():
            print("Invalid date entered, try again.")
            continue
        if not temprature.isdigit():
            print("Invalid temprature entered, try again.")
            continue
        if not humidity.replace("%", "").isdigit():
            print("Invalid humidity entered, try again.")
            continue
        if city not in weatherInfo:
            weatherInfo[city] = {"date": date, "temprature": temprature, "humidity": humidity, "condition": weatherCondition}
            moreEntryChoice: str = input("Do you want to add another city? (yes/no)")
            if moreEntryChoice == "yes":
                continue
            else:
                return weatherInfo
        else:
            print("City already exists")
            

#Searching for a specific city and retreiving its info
def displayCity(city: str, weatherInfo : dict):
    '''
    This function takes the name of the city the user wants to find and the weather information dictionary as args
    and prints the information of that city if it exists
    '''
    if city in weatherInfo:
        print(f"City name: {city}.")
        print(f"Date: {weatherInfo[city]["date"]}")
        print(f"Temprature: {weatherInfo[city]["temprature"]} degrees.")
        print(f"Humidity: {weatherInfo[city]["humidity"]}% .")
        print(f"Weather condition: {weatherInfo[city]["condition"]}.")
    else:
        print("City info doesn't exist")

#Creating an empty dictionary 
weatherData: dict = {}

while True:
    print("---Welcome to Weather Data---")

    #Make user choose the query
    choice: str = input("Please choose your query:\n 1. Add new city.\n 2. Display a specefic city\n 3. Exit ")

    if choice == "1":
        #storing the created dictionary in the empty dictionary variable
        weatherData = weatherDictAdd()
        continue
    elif choice == "2":
        #Finding city by name
        city: str = input("Enter the name of the city you want to display: ")
        displayCity(city, weatherData)
        break
    elif choice == "3":
        print("Program ended")
        break
    else:
        print("Invalid choice, try again.")
        continue