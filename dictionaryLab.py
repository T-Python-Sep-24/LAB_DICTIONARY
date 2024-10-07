# Question 1

''' ## Q1:Build a phone book program that receives the phone number
 (Use Input to let the user provide the number), and returns the name of the owner.
 
 - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
- If the number is less or more than 10 numbers, print "This is invalid number".
- If the number contains letters or symbols, print "This is invalid number".
 '''

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

    number = input("Please enter the phone number: ")

    if len(number) != 10 or not number.isdigit():
        print("This is an invalid number.")
    else:
        owner = None
        for name, phone in phone_numbers.items():
            if phone == number:
                owner = name
                break
        if owner:
            print(f"The owner of the number {number} is {owner}.")
        else:
            print("Sorry, the number is not found.")

phone_book()


# Question 2
''' ## Q2:Write a function that receives a list containing the following numbers : 
- [5, 0, 34, 9, 0, 13, 8]
- rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.'''

def rearrange_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [0] * numbers.count(0)
    return non_zeros + zeros

numbers_list = [5, 0, 34, 9, 0, 13, 8]
arranged_list = rearrange_zeros(numbers_list)
print(arranged_list)