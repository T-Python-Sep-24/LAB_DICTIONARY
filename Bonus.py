#Function for storing data into dictionary 
def weatherDictAdd():
    '''
    This function prompts the user to enter weather details of a city then stores it in a nested dictionary 
    after validating the info
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
            #Check that the city doesn't exist first
            if city not in weatherData:
                weatherData[city] = {"date": date, "temprature": temprature, "humidity": humidity, "condition": weatherCondition}
                moreEntryChoice: str = input("Do you want to add another city? (yes/no) ")
                if moreEntryChoice == "yes":
                    continue
                else:
                    break
            else:
                print("City already exists")
        else: 
            print(errorMessage)

#Update/ Delete existing city info
def weatherDictUpdateDelete():
    '''
    This function updates or deletes the information of an existing city if it's found 
    '''
    #Keep prompting the user to enter a choice until they provide a valid choice
    while True:
        choice: str = input("Enter 'update' to update a city, and 'delete' to delete it: ")
        #Start of update operation
        if choice == "update":
            city: str = input("Enter the name of the city: ")
            #Make sure the city exists before performing the operation
            if city not in weatherData:
                print("City info doesn't exist")
                break
            else:    
                date: str = input("Enter the new date value (dd-mm-yyyy) : ")
                temprature: str = input("Enter the new temprature value (C): ")
                humidity: str = input("Enter the new humidity value (%): ")
                weatherCondition: str = input("Enter the new weather condition: ")
                errorMessage: str = dataValidation(city, date, temprature, humidity, weatherCondition)
                if errorMessage == " ":
                    weatherData [city]["date"] = date
                    weatherData [city]["temprature"] = temprature
                    weatherData [city]["humidity"] = humidity
                    weatherData [city]["condition"] = weatherCondition
                    break
                else:
                    print(errorMessage)
                    break
        elif choice == "delete": 
            city: str = input("Enter the name of the city: ")
            if city not in weatherData:
                print("City info doesn't exist.")
                break
            else: 
                del weatherData[city]
                print("City had been deleted successfully.")
                break
        else: 
            print("Invalid choice, try again.")
       
#Searching for a specific city and retreiving its info
def displayCity():
    '''
    This function finds if information of a city of the user's choice is in weatherData dict
    and prints the information of that city if it exists
    '''
    city: str = input("Enter the name of the city you want to display: ")
    if city in weatherData:
        print(f"City name: {city}.")
        print(f"Date: {weatherData[city]["date"]}")
        print(f"Temprature: {weatherData[city]["temprature"]} degrees.")
        print(f"Humidity: {weatherData[city]["humidity"]}% .")
        print(f"Weather condition: {weatherData[city]["condition"]}.")
    else:
        print("City info doesn't exist")

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
print("---Welcome to Weather Data---")
while True:
    #Make user choose the query
    choice: str = input(" 1. Add new city.\n 2. Display a city's info.\n 3. Update/ Delete existing city\n 4. Exit\n Please choose your query: ")
    #Calling functions based on user choice
    if choice == "1":
        #Call function  to perform adding items operation
        weatherDictAdd()
        input("")
    elif choice == "2":
        #Find city by name then display it
        displayCity()
        input("")
    elif choice == "3":
        #Update/ Delete a city in the dictionary
        weatherDictUpdateDelete()
        input("")
    elif choice == "4":
        #Exit program
        print("Program ended")
        break
    else:
        print("Invalid choice, try again.")