def Arrange(number:list)->list:
    none_zeros=[num for num in number if num!=0]
    zeros=[0]*(len(number)-len(none_zeros))
    return none_zeros+zeros

number=[5, 0, 34, 9, 0, 13, 8]
print(Arrange(number))


