#1
phone_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}


def get_owner_by_number():
  
    phone_number = input("Enter the phone number: ")
    
    
    if not phone_number.isdigit():
        print("This is invalid number")
    elif len(phone_number) != 10:
        print("This is invalid number")
    else:
        
        owner = phone_book.get(phone_number, "Sorry, the number is not found")
        print(f"Owner: {owner}")


get_owner_by_number()


#2

def rearrange_zeros(lst):
   
    non_zero_index = 0
    
   
    for i in range(len(lst)):
    
        if lst[i] != 0:
            lst[non_zero_index] = lst[i]
            non_zero_index += 1
            
   
    for i in range(non_zero_index, len(lst)):
        lst[i] = 0
    
    return lst


numbers = [5, 0, 34, 9, 0, 13, 8]


rearranged_list = rearrange_zeros(numbers)
print(rearranged_list)