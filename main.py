'''
# LAB_DICTIONARY

'''



## Q1
phone_dict={
    "0568323222":"Amal",
    "0522222232":"Mohammed",
    "0532335983":"Khadijah",
    "0545341144":"Abdullah",
    "0545534556":"Rawan",
    "0560664566":"Faisal",
    "0567917077":"Layla"}

def search_num(num:str)-> str:
    '''receives the name of the owner by its phone number '''
    if not (num.isdigit() and len(num)==10):
        return "This is invalid number"
    else:
        return phone_dict.get(num,"Sorry, the number is not found")


input_num=input("Enter phone number: ")
print(search_num(input_num))
    
## Q2

def arrange_list(list2:list) -> list:
    list2.sort(reverse=True)
    return list2

list1=[5, 0, 34, 9, 0, 13, 8]
print(arrange_list(list1))
