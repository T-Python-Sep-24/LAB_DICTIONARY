weather_data = {}


def adding_data(): 
    global city 
    global date
    global temperature
    global humidity
    global condition
    
    city = input("Enter city: ")
    date = input("Enter date (MM-DD-YYYY): ")
    temperature = input("Enter temperature: ")
    humidity = input("Enter humidity: ")
    condition = input("Enter condition (e.g., sunny, rainy): ")

    if city not in weather_data:
        weather_data[city] ={
            "date": date, 
         "temperature": temperature, 
         "humidity": humidity, 
         "condition": condition  
        }   
        print(f"Data for {city} is added successfully.")
    else:
        print("Is city exists already")

def display_data():
    city = input("Enter city to display data for: ")
    if city in weather_data:
        print(f"Weather data for city:{city}{weather_data[city]}")
    else:
        print(f"No weather data found for {city}.")


def delete_data(): 
    city = input("Enter the city to delete: ")
    cityHold = city
    if cityHold not in weather_data.items():
        # if cityHold == weather_data[city]:
            del weather_data[cityHold] 
            print(f"All data for {city} has been deleted.")
    else:
        print(f"{city} not found in the data.")


while True: 
    choice = input("Please Select:\n1 - Add city\n2 - Display city data\n3 - Delete data\n4 - Exit\n")
    
    if choice == "1":
        adding_data()
      
    elif choice == "2":
        display_data()
    
    elif choice == "3":
        delete_data()
    
    elif choice == "4":
        break
    
    else:
        print("Invalid choice. Please select again.")

