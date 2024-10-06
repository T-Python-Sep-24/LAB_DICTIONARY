# Q1 dictionaries
numbers_book = {
    "0568323222": "Amal",
    "0522222232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
phone_number = ""
while True:
    phone_number = input(">>> Enter a phone number or Q/q to exit: ")
    if phone_number.lower() == "q":
        print("Thx")
        break
    else:
        if len(phone_number) < 10 or not phone_number.isnumeric():
            print("This is an invalid number, Please try again")

        else:
            if phone_number in numbers_book:
                name = numbers_book[phone_number]
                print(f"---- Match Found ---- \n{name} : {phone_number}")
                print("-"*21)

            elif not phone_number in numbers_book:
                print("Sorry, the number is not found")


# Q2

def rearrangeList(nList):
    """
        This function takes a list and rearrange the zeros at the
        end of the list and returns it
    """
    for element in nList:
        if element == 0:
            element_index = nList.index(element)
            temp = nList.pop(element_index)
            nList.append(temp)

    return nList

print("-"*30)
numLists = [0, 5, 0, 34, 0, 9, 0, 13, 8]
print("This is the rearranged list: ", rearrangeList(numLists))
print("-"*30)