phoneBook = {
    '0568323222': 'Amal',
    '0522222232': 'Mohammed',
    '0532335983': 'Khadijah',
    '0545341144': 'Abdullah',
    '0545534556': 'Rawan',
    '0560664566': 'Faisal',
    '0567917077': 'Layla'
}

phone = input('Inter a Phone Number: ')

if len(phone) < 10 or len(phone) > 10:
    print('This is invalid number')
elif not phone.isdigit():
    print('This is invalid number, it\'s not a digit')
else:
    if phone in phoneBook:
        print('The phone number owner: ', phoneBook[phone])
    else:
        print('Sorry, the number is not found')
        
    
