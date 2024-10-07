#Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.

def get_owner(phone_number):
    phone_book = {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
        "0532335983": "Khadijah",
        "0545341144": "Abdullah",
        "0545534556": "Rawan",
        "0560664566": "Faisal",
        "0567917077": "Layla"  
    }
    
    if not phone_number.isdigit() or len(phone_number) != 10:
        return "This is an invalid number"
    
    owner = phone_book.get(phone_number)
    
    if owner is not None:
        return f"The owner of the number {phone_number} is: {owner}"
    else:
        return "Sorry, the number is not found."
    
number_input = input("Please enter a phone number: ")
print(get_owner(number_input))


#Q2:Write a function that receives a list containing the following numbers :
#[5, 0, 34, 9, 0, 13, 8]
#rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def rearrange_zeros(input_list):
    # Create a new list to hold non-zero elements
    non_zero_list = [num for num in input_list if num != 0]
    
    # Count the number of zeros
    zero_count = input_list.count(0)
    
    # Extend the non-zero list with zeros at the end
    non_zero_list.extend([0] * zero_count)
    
    return non_zero_list
numbers = [5, 0, 34, 9, 0, 13, 8]
result = rearrange_zeros(numbers)
print(result)  

# Output: [5, 34, 9, 13, 8, 0, 0]