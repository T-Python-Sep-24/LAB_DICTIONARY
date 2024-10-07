

weather_data={}
def add_data():
    """
    The function make the user add data to the dict
    Args:
        None
    Returns:
        None
    """
    city=input("Enter a city name: ").strip().lower()
    if city not in weather_data:
        weather_data[city]={}
    
    while True:
        date=input("Enter date like this format(YYYY-MM-DD): ").strip()
        if (len(date)!=10 or date[4]!='-'or date[7]!='-'):
            print("invalid date please put a correct data with this fomrat\n(YYY-MM-DD)")
        else:
            break
    if date in weather_data[city]:
        print ("You allready have a weather data for this date try update option!")
        return None
    temp=float(input("Enter Temperature (°C): "))
    humidity=float(input("Enter Humidity(%): "))
    condition = input("Enter weather condition (e.g., sunny, rainy): ").strip() 
    
    weather_data[city][date] = {
    'Temperature':temp,
    'Humidity':humidity,
    'Condition':condition
    }
    print(f"Weather data for {city} on {date} added successfully.")



def search_weather():
    city=input("Enter city to search: ")
    if city not in weather_data:
        print("city is not added try to add it")
        return 
    print(f"The records for {city} :\n")
    for date, details in weather_data[city].items():
            print(f"Date: {date}")
            print(f"  Temperature: {details['Temperature']}°C")
            print(f"  Humidity: {details['Humidity']}%")
            print(f"  Condition: {details['Condition'].capitalize()}\n")



def update_date():
    city=input("Enter city to search: ")
    if city not in weather_data:
        print("city is not added try to add it")
        return 
    while True:
        date=input("Enter date like this format(YYYY-MM-DD): ").strip()
        if (len(date)!=10 or date[4]!='-'or date[7]!='-'):
            print("invalid date please put a correct data with this fomrat\n(YYY-MM-DD)")
        else:
            break
    if date not in weather_data[city]:
        print ("there is no record with this date try to add it!")
        return 
    temp=float(input("Enter Temperature (°C): "))
    humidity=float(input("Enter Humidity(%): "))
    condition = input("Enter weather condition (e.g., sunny, rainy): ").strip() 
    weather_data[city][date] = {
    'Temperature':temp,
    'Humidity':humidity,
    'Condition':condition
    }
    print(f"Weather data for {city} on {date} updated successfully.")




def delete_data():
    city=input("Enter city to search: ")
    if city not in weather_data:
        print("city is not added try to add it")
        return 
    while True:
        date=input("Enter date like this format(YYYY-MM-DD): ").strip()
        if (len(date)!=10 or date[4]!='-'or date[7]!='-'):
            print("invalid date please put a correct data with this fomrat\n(YYY-MM-DD)")
        else:
            break
    if date not in weather_data[city]:
        print ("there is no record with this date try to add it!")
        return 
    del weather_data[city][date]
    print("record has been deleted successfully")
    if not weather_data[city]:   
        del weather_data[city] 
print("Welcome to My prgram !")
while True:
    print("1-Add data\n2-search data\n3update data\n4-delete data\n5-exit()")
    choice=input("choice: ")
    if choice=='1':
        add_data()
        input("")
    elif choice=='2':
        search_weather()
        input("")
    elif choice=='3':
        update_date()
        input("")
    elif choice=='4':
        delete_data()
        input("")
    elif choice=='5':
        break
    else:
        print("invalid inputs!.")
        input("")

print("thanks for using my program.") 
        
    
