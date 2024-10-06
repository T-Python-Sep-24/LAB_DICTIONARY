#Q1:Build a phone book program that receives the phone number (Use Input to let the user provide the number), and returns the name of the owner.
phone_book={"0568323222":"Amal","0522222232":"Mohammed","0532335983":"Khadijah","0545341144":"Abdullah","0545534556":"Rawan"
            , "0560664566":"Faisal", "0567917077":"Layla"}
number_book=input("provide the number ")
if number_book.isnumeric():
    if number_book in phone_book:
        print(f"The owner is {phone_book.get(number_book)}")
    elif len(number_book)<10 or len (number_book)<10 or number_book.isnumeric()==False:
        print("This is invalid number")
    else:
        print("Sorry, the number is not found")
#Q2:Write a function that receives a list containing the following numbers :
print("-"*15)
def rearranges_list(my_list:list):
    new_list=[]
    final_list=[]
    for i in range(0,len(my_list)):
        if my_list[i]==0:
         new_list.append(my_list[i])
        if my_list[i] !=0:
             final_list.append(my_list[i])
    final_list.extend(new_list)
    return final_list
print(rearranges_list([5, 0, 34, 9, 0, 13, 8]))
            