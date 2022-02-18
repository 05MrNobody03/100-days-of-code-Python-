
print('Hello World!')

#strings : like perl necklace  and ' shows
#          the beggining and end of the string

print('Day 1 - Python Print Function')
print('this function is declared like this:')
print("ptint('what to print')")
print('print("what to print")')
print("___________________________________________")


# string manipulation: 
# new line in print

print('Day 1 - Python Print Function\nthis function is declared like this:\nprint("what to print")')

# String concatination:


print("this is without space: "+"Hey"+"NINJA")
print("this is with space: "+"Hey"+" "+"NINJA")

print("___________________________________________")

# indentation error:

print("hey NINJA")
#   print("Hey NINJA")

print("___________________________________________")

# find error in below code:

''' 
print(Day 1 - string Manipulation')
print("String concatination is done with"+"sign")
    print('e.g. print("Hello"+"World")')
print(("New line can be created with a backslash and n")

'''
# corrections are as follows:


print('Day 1 - string Manipulation')
print("String concatination is done with"+"+"+"sign")
print('e.g. print("Hello"+"World")')
print("New line can be created with a backslash and n")

print("___________________________________________")

#input function: To take input from users
input('your name is? ')
print('hello '+ input('enter your name:'))

# print no of characters in input name:

print(len(input('what is your name: ')))

#variables = containers to store info

#name=input("enter your name:")
#print(name)

name= "NINJA"
print(name)

# interchange a and b variables:

a=int(input('a= '))
b= int(input("b= "))
temp=a
a=b
b=temp
print("a= ",a)
print("b= ",b)
print("___________________________________________")

# naming variables:

# start with alphabet or _ only
# can contain only alphabet, numbers or _
# dont use keywords as names of variables
_name='pratik'
print(_name)

print("___________________________________________")

#Brand Name Generator:

city=input('enter your city name: ')
pet=input('enter your pet name: ')
print('your brand name might be: ', city+ " " + pet)
