from math import *
#print('Hello World,welcome')

#name = 'Tamara'
#age = 22
#print(name+' is a girl')
#print(name+' is ', age)
#print(name+' is From egypt')


#print('Hi.\nHow are you')
#print('Hi.\How are you')
#print(name.replace('m','T'))


#numbers
number = 55
number2 =str(number)
print(2+3)
print(62+37.764)
print(62/37.764)
print(30%4)
print(23)
print(number)
print(number2)
print('The number is '+number2)
print(-5)
print(abs(-5))
print(max(4,2))
print(max(4,2,8,22))
print(min(4,2,8,22))
print(round(3.2))
print(bin(3))
print(bin(334))
print(sqrt(9))

##getting input from user
name = input('Input your name: ')
age = int(input('Input your age: '))
print('Hello '+name+' you are ',age,' years old')

coun_file = open("C:/Users/user/OneDrive/Desktop/Python Backend/countries.txt","r")#read
print(coun_file.readline())
coun_file.close()

#open('countries.txt','w')#write
#open('countries.txt','a')#append
#open('countries.txt','r+')#read and write
#open('countries.txt','w+') #create a file if not exist
#open('countries.txt','a+')#append and create a file if not exist
#open('countries.txt','x')#create a file if not exist
