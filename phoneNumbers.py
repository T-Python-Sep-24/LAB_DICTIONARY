def number_book(phone:str,phone_dict:dict)->str:
    '''
    The function Tries to find the owner of the number in the dictionary
    Args:
        phone (str): this value contains the user input 
        phone_dict (dict): this is the dictionary that has all the phone numbers with thier owner
    Returns:
        if it was found in the dict it will return the owner of the number 
        if not returns that the number was not found
    '''
    for key,value in phone_dict.items():
        if phone==value:
            return key
        else:
            return "Sorry, the number is not found "

phone_dict ={
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}
user_input=input("write a number to check it's owner: ")

if user_input.isdigit() and len(user_input)==10:
    print(number_book(user_input,phone_dict))
else:
    print("This is invalid number,\nNumber must be 10 characters long and\ndoesn't contain letters or symbols")