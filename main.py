dictData = { 
    "Amal": "0568323222", 
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

# Input the phone number
phone_number = input("Enter the phone number: ")

#Find the owner of the phone number
for name, number in dictData.items():
    if number == phone_number:
        print(f"The owner of the number is {name}.")
        break
    
    #Check if the phone number is 10 digits
    # This is condition number is less or more than 10 number    
    elif len(phone_number) < 10 or len(phone_number) != 10:
        print("This is an invalid number.")
        break

    # Check if the phone number contains only digits
    # This is condition for number contains letters or symbols
    elif not phone_number.isdigit():
        print("This is an invalid number")
        break
else:
    print("Sorry, the number is not found.")


print("-"*20)

def move_zeros_to_end(numbers):
    '''
    Moves all zeros in the list to the end while maintaining the order of non-zero elements.

    This function iterates through the input list, identifies zeros, removes them,
    and appends them to the end of the list. The original list is modified in place.

    Args:
        numbers (list): A list of integers where zeros need to be moved to the end.

    Returns:
        list: The modified list with all zeros moved to the end.
    '''
    
    for countNum in numbers:
        if countNum == 0:
            numbers.remove(countNum)
            numbers.append(0)
    return numbers


numbers_list = [5, 0, 34, 9, 0, 13, 8]
result = move_zeros_to_end(numbers_list)
print(result)  