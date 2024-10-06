def contacts():

    phone_numbers = {

       "0568323222": "Amal " ,
       "0522222232": "Mohammed",
       "0532335983": "Khadijah" ,
       "0545341144": "Abdullah" ,
       "0545534556": "Rawan" ,
       "0560664566":"Faisal",
       "0567917077": "Layla"
        }
    
    number = input("enter the phone number : ")

    if len(number) != 10 or not number.isdigit():
        print("this is invalid number")
        return
    
    contact = phone_numbers.get(number)

    if contact:
        print("the contact for the number is: ",contact)
    else:
        print("sorry, the number is not found")

contacts()

def move(numbers):

    zeroElements = [num for num in numbers if num != 0]
    zeroCount = numbers.count(0) 
    zeroElements.sort(reverse=True)#sort non-zero elements in descending order
    zeroElements.extend([0]*zeroCount )
    return zeroElements


numbers = [5, 0, 34, 9, 0, 13, 8]
result = move(numbers)
print(result)



