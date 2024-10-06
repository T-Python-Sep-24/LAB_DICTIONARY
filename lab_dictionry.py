phonebook = {
    "0568323222": "Amal",
    "05222252232": "Mohammed",
    "0532335983": "Khadijah",
    "0545341144": "Abdullah",
    "0545534556": "Rawan",
    "0560664566": "Faisal",
    "0567917077": "Layla"
}
interTheNum=str(input("Enter a number: "))

def get_phone_number( number):
    searcher= len(interTheNum)
    if not interTheNum.isdigit():
        print("This is invalid number")
    elif searcher <10  or searcher>10:
        print("This is invalid number")
    elif number in phonebook:
            print(f" Number: {number} for {phonebook[number]}")

    else:
        print(f"No record found for {interTheNum}")
get_phone_number(interTheNum)
list_number=[5, 0, 34, 9, 0, 13, 8]
def list_last(n):
    lister=[n for n in list_number if n !=0]
    list_zero=[n for n in list_number if n ==0]
    result= lister+list_zero
    return result


print(list_last(list_number))