"""
1: Build a phone book program that receives the phone number 
(Use Input to let the user provide the number), and returns the name of the owner.
"""
phoneBookDict = { 
    "Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"
}

number = input("Number: ")
# If the number is less or more than 10 numbers, print "This is invalid number".
if len(number) != 10:
    print("This is invalid number")
# If the number contains letters or symbols, print "This is invalid number".
elif not number.isnumeric():
    print("This is invalid number")
else:
    # If the number exists, print the owner. Otherwise, print Sorry.
    for key, value in phoneBookDict.items():
        if number == value:
            print(f"Owner: {key}")
            break
    else:
        print("Sorry, the number is not found")



"""
2: Rearranges the list 
"""
def rearrangeList(orgList: list) -> list:
    '''
    Rearange the list so that zeros are at the end

    Args:
        orgList (list): a list contain original value

    Returns:
        list: the arranged list
    '''

    newList = []
    zerosList = []

    for item in orgList:
        if item != 0:
            newList.append(item)
        else:
            zerosList.append(item)
    newList.extend(zerosList)

    return newList

arrangedList = rearrangeList([5, 0, 34, 9, 0, 13, 8])
print("=" * 40)
print(f"Arranged List: {arrangedList}")