#task1
contacts = {"Amal": "0568323222",
    "Mohammed": "0522222232",
    "Khadijah": "0532335983",
    "Abdullah": "0545341144",
    "Rawan": "0545534556",
    "Faisal": "0560664566",
    "Layla": "0567917077"}
while True:
    number = input("Enter a number: ")
    if len(number) <10 or not number.isdigit():
        print("This is invalid number")
    else:
        name1= None
        for name, num in contacts.items():
            if number == num:
                name1 = name
                print(f"the owner name of the number: {number}, is: {name1}")
                break
        if name1 is None:
            print("Sorry, the number is not found")
        break        
            
#task2
def arranged_list(list) :
    non_zero=[]
    zero= []
    for n in list:
        if n == 0:
            zero.append(n)
        else:
            non_zero.append(n)
    return non_zero + zero
list= [5, 0, 34, 9, 0, 13, 8]
result= arranged_list(list)
print(result)