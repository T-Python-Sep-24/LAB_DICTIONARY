#Q1 answer:
#Dictionary of every number and its corresponding name
numberBook = {"0568323222": "Amal",
             "0522222232": "Mohammed",
             "0532335983": "Khadijah",
             "0545341144": "Abdullah",
             "0545534556": "Rawan",
             "0560664566": "Faisal",
             "0567917077": "Layla"}

#Ask user for phone number 
phone: str = input("Please enter a phone number: ")


#Check the string the user entered is numbers only and the length is 10
if phone.isdigit and len(phone) != 10:
    print("This is an invalid number.")

else:
    #Checking if number exists
    print(numberBook.get(phone, "Sorry, the number is not found."))

#Q2 answer:
def rearrangeList(numbers:list) -> list:
    '''
    This function rearranges the list so that the zeros are the end of the list, then returns the arranged list
    '''

    modifiedList: list = list()
    for n in numbers:
        if n == 0:
            modifiedList.append(n)
        else:
            modifiedList.insert(0, n)
    return modifiedList

#Defining a list of numbers 
numbers: list = [5, 0, 34, 9, 0, 13, 8]

#Call the function to arrange the list so that zeroes are at the end
arrangedNumbers: list = rearrangeList(numbers)
print(arrangedNumbers)