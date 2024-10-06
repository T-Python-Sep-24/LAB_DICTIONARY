def add_dict(**dict):
    return dict
weather={}
answer=""
while answer !="n":
    city=input("Enter city name ")
    date=input("Enter date ")
    temperature=input("Enter temperature ")
    humidity=input("Enter humidity ")
    weather_condition=input("Enter weather condition ")
    value=add_dict(date=date , temperature=temperature , humidity=humidity , weather_condition=weather_condition)
    weather[city]=value
    find_data=input("Enter the city name to find it ")
    if find_data in weather.keys():
        print(weather[find_data])
    else: 
        print("Not found")
    update1=input("to update enter space for otherwise")
    if not update1.isspace():
        update_d=input("Enter the date")
        update_temperature=input("Enter temperature")
        update_humidity=input("Enter humidity")
        update_weather_condition=input("Enter weather_condition")
        update_value=add_dict(update_d=update_d , update_temperature=update_temperature , update_humidity=update_humidity , update_weather_condition=update_weather_condition)
        weather[update1]=update_value

    print(weather)
