#Lab 8

#Answe Q1

# Phonebook dictionary
my_dic = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

userNumber = input("Please Enter your Phone Number: ")

# Function to check phone number
def check_numbers(userNumber: str):
    # Validate the number length
    if len(userNumber) != 10:
        return "This is invalid number"
    
    # Validate if the number contains only digits
    if not userNumber.isdigit():
        return "This is invalid number"
    
    # Check if the number exists in the phonebook
    for name, number in my_dic.items():
        if number == userNumber:
            return f"The owner of the number is {name}"
    
    # If the number is not found in the dictionary
    return "Sorry, the number is not found"

result = check_numbers(userNumber)
print(result)


#Answer Q2

def rearrange_list(input_list):
    # Separate non-zero numbers
    non_zero_numbers = [num for num in input_list if num != 0]
    
    zero_count = input_list.count(0)
    
    rearranged_list = non_zero_numbers + [0] * zero_count
    
    return rearranged_list

input_list = [5, 0, 34, 9, 0, 13, 8]
result = rearrange_list(input_list)
print(result)
