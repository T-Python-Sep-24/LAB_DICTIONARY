#Function for storing data into dictionary 
def weatherDictAdd(weatherInfo: dict):
    '''
    This function prompt user to enter city weather data as args and stores it in nested dictionariesa after validating the info
    '''
    while True:
        city: str = input("Enter the city's name: ")
        date: str = input("Enter the date (dd-mm-yyyy): ")
        temprature: str = input("Enter the temprature (C): ")
        humidity: str = input("Enter the humidity (%): ")
        weatherCondition: str = input("Enter the weather condition: ")
        #Call dataValidation() to check data validty
        errorMessage: str = dataValidation(city, date, temprature, humidity, weatherCondition)
        #If the dataValidation function returned an empty string it means there was no error
        if errorMessage == " ":
            if city not in weatherInfo:
                weatherInfo[city] = {"date": date, "temprature": temprature, "humidity": humidity, "condition": weatherCondition}
                moreEntryChoice: str = input("Do you want to add another city? (yes/no) ")
                if moreEntryChoice == "yes":
                    continue
                else:
                    return weatherInfo
            else:
                print("City already exists")
        else: 
            print(errorMessage)
            
#Searching for a specific city and retreiving its info
def displayCity(weatherInfo : dict):
    '''
    This function takes the name of the city the user wants to find and the weather information dictionary as Args
    and prints the information of that city if it exists
    '''
    city: str = input("Enter the name of the city you want to display: ")
    if city in weatherInfo:
        print(f"City name: {city}.")
        print(f"Date: {weatherInfo[city]["date"]}")
        print(f"Temprature: {weatherInfo[city]["temprature"]} degrees.")
        print(f"Humidity: {weatherInfo[city]["humidity"]}% .")
        print(f"Weather condition: {weatherInfo[city]["condition"]}.")
    else:
        print("City info doesn't exist")

#Update existing city info
def weatherDictUpdate(weatherInfo: dict):
    '''
    This function updates the info of an existing city if it's found 
    '''
    city: str = input("Enter the name of the city you want to update: ")
    if city not in weatherInfo:
        print("City info doesn't exist")
    else:    
        date: str = input("Enter the new date value (dd-mm-yyyy) : ")
        temprature: str = input("Enter the new temprature value (C): ")
        humidity: str = input("Enter the new humidity value  (%): ")
        weatherCondition: str = input("Enter the new weather condition: ")
        errorMessage: str = dataValidation(city, date, temprature, humidity, weatherCondition)
        if errorMessage == " ":
            weatherInfo [city]["date"] = date
            weatherInfo [city]["temprature"] = temprature
            weatherInfo [city]["humidity"] = humidity
            weatherInfo [city]["condition"] = weatherCondition
        else:
            print(errorMessage)        

#Function to validate data and return the error message if not valid
def dataValidation(city: str, date: str, temprature: str, humidity: str, condition: str) -> str : 
    '''
    This function takes weather data as Args and performs check ups to make sure data is valid
    if the data is not valid return an error message to the user
    '''
    if city == " " or date == " " or temprature == " " or humidity == " " or condition == " ":
        return "Please fill all fields!"
    if not date.replace("-", "").isdigit():
        return "Invalid date entered, try again."
    if not temprature.isdigit():
        return "Invalid temprature entered, try again."
    if not humidity.replace("%", "").isdigit():
        return "Invalid humidity entered, try again."
    
    return " "

#Creating an empty dictionary 
weatherData: dict = {}

#Main program
while True:
    print("---Welcome to Weather Data---")
    #Make user choose the query
    choice: str = input(" 1. Add new city.\n 2. Display a city's info.\n 3. Update existing city\n 4. Exit\n Please choose your query: ")
    #Calling functions based on user choice
    if choice == "1":
        #Store the created dictionary in the empty dictionary variable
        weatherData = weatherDictAdd(weatherData)
        continue
    elif choice == "2":
        #Find city by name then display it
        displayCity(weatherData)
        continue
    elif choice == "3":
        weatherDictUpdate(weatherData)
        continue
    elif choice == "4":
        print("Program ended")
        break
    else:
        print("Invalid choice, try again.")
        continue