# LAB_DICTIONARY


## Q1:Build a phone book program that receives the phone number 
# (Use Input to let the user provide the number), and returns the name of the owner. 
phone_book= {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}

number_exists = input("Enter number phone : ")

if number_exists.isdigit() and len(number_exists) == 10:
    result = phone_book.get(number_exists)
    if result:
        print(result)
    else:
        print('Sorry, the number is not found')
else:
    result = 'This is invalid number'
    print(result)

def rearrange_list(nums):

    non_zeros = [num for num in nums if num != 0]
    
    zeros = [num for num in nums if num == 0]
    
    return non_zeros + zeros

numbers = [5, 0, 34, 9, 0, 13, 8]

rearranged = rearrange_list(numbers)
print(rearranged)

