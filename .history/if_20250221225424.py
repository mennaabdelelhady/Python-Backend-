a= 2 
b =3 
if a < b:
    print('a is less than b')
elif a == b:
    print('a is equal to b')    
else:
    print('a is greater than b')    


value = input('Enter a value: ')

if type(value) == int:
    print('This is an integer')
elif type(value) == str:
    print('This is a string')
elif type(value) == list:
    print('This is a list') 
else:
    print('we do not know the type')           