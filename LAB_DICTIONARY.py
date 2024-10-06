def phone_book():
    phone_numbers = {
        "Amal": "0568323222",
        "Mohammed": "0522222232",
        "Khadijah": "0532335983",
        "Abdullah": "0545341144",
        "Rawan": "0545534556",
        "Faisal": "0560664566",
        "Layla": "0567917077"
    }

    number = input("Enter the phone number: ")
    
    if len(number) != 10 or not number.isdigit():
        return print("This is an invalid number.")
    
    owner = next((name for name, num in phone_numbers.items() if num == number), None)
    print(f"The owner of the number is: {owner}" if owner else "Sorry, the number is not found.")

def rearrange_zeros(numbers):
    return [num for num in numbers if num != 0] + [0] * numbers.count(0)

def input_weather_data(weather_data):
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    weather_data.setdefault(city, {})[date] = {
        "temperature": input("Enter temperature: "),
        "humidity": input("Enter humidity: "),
        "condition": input("Enter weather condition: ")
    }

def query_weather_data(weather_data):
    city = input("Enter city name to query: ")
    if city in weather_data:
        for date, details in weather_data[city].items():
            print(f"{date}: {details}")
    else:
        print("City not found.")

def main():
    weather_data = {}
    
    while True:
        print("\n1. Phone Book\n2. Rearrange Zeros\n3. Input Weather Data\n4. Query Weather Data\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            phone_book()
        elif choice == '2':
            numbers_list = [5, 0, 34, 9, 0, 13, 8]
            arranged_list = rearrange_zeros(numbers_list)
            print("Rearranged List:", arranged_list)
        elif choice == '3':
            input_weather_data(weather_data)
        elif choice == '4':
            query_weather_data(weather_data)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

# Run the main program
main()
