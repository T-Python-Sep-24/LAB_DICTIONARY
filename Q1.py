def find_owner(phone_number):
    phone_book = {
        "0568323222": "Amal",
        "0522222232": "Mohammed",
    }
    if not phone_number.isdigit() or len(phone_number) != 10:
        return "This is an invalid number"
    owner = phone_book.get(phone_number)
    if owner is not None:
        return owner
    else:
        return "Sorry, the number is not found"
phone_number = input("enter the phone number: ")
print("the owner is ",find_owner(phone_number))