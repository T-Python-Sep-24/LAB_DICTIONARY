phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan":  "0545534556",
    "Faisal":   "0560664566",
    "Layla":  "0567917077"
}

phone_number = input("provide your number:")

if len(phone_number) != 10 or not phone_number.isdigit():
    print("This is invalid number")
else:
    owner = None
    for name, number in phone_book.items():
        if number == phone_number:
            owner = name
            break

   
    if owner:
        print(f"The owner is {owner}")

    else:
        print("Sorry, the number is not found") 


print()
def rearrange_list(numbers):
    
    non_zero_num = [num for num in numbers if num != 0]
    zero_num = [num for num in numbers if num == 0]
    
    
    arranged_list = non_zero_num + zero_num
    
    return arranged_list

numbers = [5, 0, 34, 9, 0, 13, 8]

print("The list: ", rearrange_list(numbers))
