def arrangeList(orginal_list:list):
    new_list = []
    zeros_list = []
    for num in orginal_list:
        if num != 0:
            new_list.append(num)
        else:
            zeros_list.append(num)
            
    for zero in zeros_list:
        new_list.append(zero)
    
    return new_list

theList = [5, 0, 34, 9, 0, 13, 8]

print(arrangeList(theList)) 
