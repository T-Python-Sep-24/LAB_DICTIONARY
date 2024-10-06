# Phone book dictionary
phone_book = {
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

# Function to find the owner by phone number
def find_owner(phone_number):
    # Check if the phone number is valid
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("This is an invalid number.")
        return

    # Check if the phone number exists in the phone book
    for name, number in phone_book.items():
        if number == phone_number:
            print(f"The owner of the number {phone_number} is {name}.")
            return

    print("Sorry, the number is not found.")

# Main program
user_input = input("Please enter a phone number: ")
find_owner(user_input)

#-------------------------------------------------------------
#Q2:Write a function that receives a list containing the following numbers :
# [5, 0, 34, 9, 0, 13, 8]
#rearranges the list so that the zeros are the end of the list, and finally returns the arranged list.

def move_zeros_to_end(num_list):
    # Create a new list for non-zero elements
    non_zeros = [num for num in num_list if num != 0]
    # Count the number of zeros
    zeros = [0] * num_list.count(0)
    # Combine non-zero elements with the zeros at the end
    return non_zeros + zeros

# Example list
numbers = [5, 0, 34, 9, 0, 13, 8]
# Call the function and print the result
result = move_zeros_to_end(numbers)
print("Rearranged list:", result)
