from datetime import date

Cities = {}

stop = True
while stop:
    weather = {}
    city = input('Inter a city: ')
    current_date = date.today().isoformat()
    temperature = input('What is the temperature in your city in C? ')
    humidity = input('How is the humidity in %? ')
    weather_condition = input('What is the weather_condition (e.g., sunny, rainy)? ')
    
    weather.update({
        "date": current_date,
        "temperature": temperature,
        "humidity": humidity,
        "weather_condition": weather_condition 
    })
    
    Cities[city] = weather
    
    print()
    flag = input('Do you want to inter a new City, y or n?')
    if flag == 'n':
        stop = False

print()
print('The Query Part:>>>')
print()
stopQuery = True
while stopQuery:
    search = input('Do you want to query weather data by City, y or n?')
    if search == 'y':
        city_name = input('Inter a city to display weather data: ')
        if city_name in Cities:
            weather_data = Cities[city_name]
            for key, value in weather_data.items():
                print(f'The {key} is {value}.')
        else:
            print('The city does not exist!')
    else:
        stopQuery = False
    print()
    flag_query = input('Do you want to query weather data for another City, y or n?')
    if flag_query == 'n':
        stopQuery = False
        
print()
print('Goodbay! ')