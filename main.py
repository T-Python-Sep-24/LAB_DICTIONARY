phone_book = {
    "0599999999" : "Eyad",
    "0588888888" : "hamza",
    "0566666666" : "amal",
    "0555555555" : "ghala",
    "0544444444" : "jehad",
    "0533333333" : "aqeel"
    }
user_input = input("Enter a phone number: ")
if user_input in phone_book:
    print(f"the name of the owner this number {user_input} is {phone_book[user_input]}")
else:
    print(f"Sorry we don't have the info for {user_input}")