'''
# Bonus

'''

def entry_weather_data()-> dict:
    data_dict={}
    while True:
        city = input("Enter the city name (or type 'exit' to finish): ")
        if not city.isalpha():
            print("your input is not valid")
            break
        if city.lower() == 'exit':
            break  
        
        date = str(input("Enter the date as (dd-mm-yyyy): "))
        if not (date[0:2]).isdigit and date[2]=="-" and (date[3:5]).isdigit and date[5]=="-" and (date[6:]).isdigit:
             print("your input is not valid")
             break
        temperature = input("Enter the temperature: ")
        if not temperature.isdigit():
            print("your input is not valid")
            break
        humidity = input("Enter the humidity: ")
        if not humidity.isdigit():
            print("your input is not valid")
            break
        condition = input("Enter the weather condition (e.g., sunny, rainy): ")
        if not condition.isalpha():
            print("your input is not valid")
            break
        data_dict[city] = {
            'date': date,
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition
        }
    return data_dict
    
        
def query_weather_data(input_dict:dict):
    city=input("Enter city name you want to show its weather data: ")
    if city in input_dict:
        details = input_dict[city]
        
        print(f"The weather in {city} on {details['date']} is:")
        print(f"Temperature: {details['temperature']}°C")
        print(f"Humidity: {details['humidity']}%")
        print(f"Weather Condition: {details['condition']}")
    else:
        print("City not found.")




# calling the functions
d1=entry_weather_data()
query_weather_data(d1)

